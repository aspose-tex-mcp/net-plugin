"""TeX worker regression tests using real source pages and isolated subprocesses."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from adcs_tex_net import gist_examples, worker

MANIFEST = json.loads((ROOT / 'plugin.json').read_text())


def request(kind, relative, text=None):
    source = MANIFEST['sources'][kind]
    repo = ROOT / 'tests/fixtures' / kind
    return dict(
        contract=MANIFEST['contract'], plugin_id=MANIFEST['plugin_id'],
        product_id=MANIFEST['product_id'], language='net', operation='extract',
        source_kind=kind, repo_id=source['repo_id'], product_family='aspose',
        source_path=source['path'] + '/' + relative, relative_repo_path=relative,
        source_prefix=source['prefix'], layout_detection=source['layout'],
        canonical_base_url=source['canonical_base_url'], source_revision='fixture',
        repo_root=str(repo), raw_markdown=text if text is not None else (repo / relative).read_text(),
    )


class TeXContractTests(unittest.TestCase):
    def test_manifest_has_tex_sources_and_no_retrieval_profile(self):
        self.assertEqual(MANIFEST['plugin_id'], 'aspose.tex.net')
        self.assertEqual(MANIFEST['product_id'], 'aspose.tex')
        self.assertNotIn('retrieval_profile', MANIFEST)
        self.assertFalse((ROOT / 'retrieval-profile.json').exists())
        self.assertEqual(MANIFEST['sources']['docs']['branch'], 'main')
        self.assertEqual(MANIFEST['sources']['docs']['prefix'], 'en/net')
        self.assertEqual(MANIFEST['sources']['apiref']['branch'], 'master')
        self.assertEqual(MANIFEST['sources']['apiref']['prefix'], 'english/net')

    def test_actual_api_classes_preserve_tex_namespace_and_type_casing(self):
        for relative, expected in [
            ('aspose.tex/texjob', 'Aspose.TeX.TeXJob'),
            ('aspose.tex/texoptions', 'Aspose.TeX.TeXOptions'),
            ('aspose.tex.io/outputfilesystemdirectory', 'Aspose.TeX.IO.OutputFileSystemDirectory'),
            ('aspose.tex.presentation.pdf/pdfsaveoptions', 'Aspose.TeX.Presentation.Pdf.PdfSaveOptions'),
        ]:
            with self.subTest(relative=relative):
                output = worker.handle(request('apiref', 'english/net/' + relative + '/_index.md'))
                self.assertTrue(output['chunk_records'])
                self.assertEqual(output['symbols'][0]['member_fqn'], expected)
                self.assertEqual(output['symbols'][0]['product'], 'aspose.tex')
                self.assertTrue(output['symbols'][0]['canonical_url'].startswith(
                    'https://reference.aspose.com/tex/net/'))

    def test_actual_constructor_overloads_preserve_declaring_type(self):
        output = worker.handle(request('apiref', 'english/net/aspose.tex/texjob/texjob/_index.md'))
        rows = output['symbols']
        self.assertEqual(len(rows), 3)
        for row in rows:
            self.assertEqual(row['kind'], 'constructor')
            self.assertEqual(row['member_fqn'], 'Aspose.TeX.TeXJob.TeXJob')
            self.assertEqual(row['parent_fqn'], 'Aspose.TeX.TeXJob')
        self.assertEqual(len({r['signature'] for r in rows}), 3)

    def test_actual_method_and_property(self):
        cases = [('texjob/run', 'Aspose.TeX.TeXJob.Run', 'method'),
                 ('texoptions/outputworkingdirectory', 'Aspose.TeX.TeXOptions.OutputWorkingDirectory', 'property')]
        for relative, expected, kind in cases:
            with self.subTest(relative=relative):
                output = worker.handle(request('apiref', 'english/net/aspose.tex/' + relative + '/_index.md'))
                self.assertEqual(output['symbols'][0]['member_fqn'], expected)
                self.assertEqual(output['symbols'][0]['kind'], kind)

    def test_actual_documentation_is_tex_scoped(self):
        output = worker.handle(request('docs', 'en/net/getting-started/supported-file-formats/_index.md'))
        self.assertTrue(output['chunk_records'])
        self.assertTrue(all(row['product_id'] == 'aspose.tex' for row in output['chunk_records']))
        self.assertEqual(output['normalized_document']['document']['canonical_url'],
                         'https://docs.aspose.com/tex/net/supported-file-formats/')

    def test_section_locale_placeholder_and_highlight_theme(self):
        text = '''---
title: Rendering
url: /net/rendering/
---
{{<section overview>}}
# Rendering
See [guide](/tex/{{lang.url-fragment}}net/guide/).
{{< emoticons/tick >}}
{{< highlight csharp >}}
var options = TeXOptions.ConsoleAppOptions(TeXConfig.ObjectLaTeX);
{{< /highlight >}}
'''
        output = worker.handle(request('docs', 'en/net/rendering/_index.md', text))
        encoded = json.dumps(output['normalized_document'])
        self.assertNotIn('{{lang.url-fragment}}', encoded)
        self.assertTrue(output['page']['code_blocks'])
        self.assertNotIn('Unsupported shortcode `section`', json.dumps(output))

    def test_real_gist_page_uses_checksummed_offline_examples(self):
        relative = 'en/net/developer-guide/conversion/latex-to-pdf/_index.md'
        req = request('docs', relative)
        code = 'var options = TeXOptions.ConsoleAppOptions(TeXConfig.ObjectLaTeX);'
        entry = dict(code=code, sha256=hashlib.sha256(code.encode()).hexdigest(), revision='a' * 40)
        cache = {'schema': 1, 'examples': {gist_examples.key(ref): entry
                                        for _, ref in gist_examples.references(req['raw_markdown'])}}
        with patch.object(gist_examples, 'read_cache', return_value=cache):
            output = worker.handle(req)
        self.assertIn(code, json.dumps(output['page']['code_blocks']))
        self.assertEqual(output['normalized_document']['document']['canonical_url'],
                         'https://docs.aspose.com/tex/net/latex-to-pdf/')

    def test_gist_cache_missing_or_corrupt_fails(self):
        req = request('docs', 'en/net/developer-guide/conversion/latex-to-pdf/_index.md')
        with patch.object(gist_examples, 'read_cache', return_value={'schema': 1, 'examples': {}}):
            with self.assertRaisesRegex(ValueError, 'Missing Gist'):
                worker.handle(req)
        with self.assertRaises(ValueError):
            gist_examples.checked_code(dict(code='code', sha256='bad', revision='a' * 40))

    def test_other_product_and_platform_requests_are_rejected(self):
        req = request('apiref', 'english/net/aspose.tex/texjob/_index.md')
        for changes in [{'product_id': 'aspose.words'}, {'plugin_id': 'aspose.words.net'}, {'language': 'java'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                worker.handle({**req, **changes})

    def test_discovery_is_limited_to_selected_prefix(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for relative in ['en/net/one.md', 'en/java/two.md']:
                p = root / relative
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('# Page')
            req = dict(contract=MANIFEST['contract'], plugin_id='aspose.tex.net', product_id='aspose.tex',
                       language='net', source_kind='docs', operation='discover', repo_root=temp,
                       source_prefix='en/net')
            self.assertEqual(worker.handle(req)['files'], ['en/net/one.md'])
            with self.assertRaises(ValueError):
                worker.handle({**req, 'source_prefix': '../escape'})

    def test_source_launcher_works_in_isolated_process(self):
        req = request('apiref', 'english/net/aspose.tex/texjob/_index.md')
        result = subprocess.run([sys.executable, '-I', str(ROOT / 'worker.py')],
                                input=json.dumps(req), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(json.loads(result.stdout)['plugin_id'], 'aspose.tex.net')

    def test_bom_and_fallback_canonical_url(self):
        output = worker.handle(request('docs', 'en/net/example/_index.md', '\ufeff# Example\nTeX content.'))
        self.assertEqual(output['normalized_document']['document']['canonical_url'],
                         'https://docs.aspose.com/tex/net/example/')


if __name__ == '__main__':
    unittest.main()
