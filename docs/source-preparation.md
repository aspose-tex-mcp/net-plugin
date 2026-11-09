# Source preparation

`plugin.json` defines repository URLs, branches, prefixes, and layout metadata. Source paths are relative to the ingestion workspace. Use this checkout as the workspace for the commands below.

```sh
mkdir -p sources
git clone --filter=blob:none --sparse --branch main https://github.com/aspose-tex-mcp/docs.git sources/documentation
git -C sources/documentation sparse-checkout set en/net
git clone --filter=blob:none --sparse --branch master https://github.com/aspose-tex-mcp/reference.git sources/api-reference
git -C sources/api-reference sparse-checkout set english/net
```

For existing source checkouts, update their remotes before synchronization:

```sh
git -C sources/documentation remote set-url origin https://github.com/aspose-tex-mcp/docs.git
git -C sources/api-reference remote set-url origin https://github.com/aspose-tex-mcp/reference.git
```

Preserve any local source changes before synchronization. A URL change does not refresh published indexes; synchronize sources and run ingestion/publication to update indexed content.

## Prepare Gist examples

After creating the virtual environment from the README:

```sh
PYTHONPATH=src .venv/bin/python -m adcs_tex_net.gist_examples --source-root sources/documentation/en/net --cache sources/gist-examples.json
```

This explicit network step fetches referenced public Gist files and records pinned revisions and checksums. Existing valid entries remain pinned unless `--refresh` is requested. Extraction is offline and fails explicitly if a required cache entry is missing or invalid. Keep the default cache location; a custom preparation output does not change the worker's cache lookup. Do not prepare the cache concurrently.

## Validate the full sources

```sh
.venv/bin/python scripts/audit_sources.py --docs-root sources/documentation --api-root sources/api-reference --output /tmp/tex-source-audit.json
```

The audit checks extraction and records source revisions, counts, warnings, and errors. It does not publish data or test an MCP deployment. The checked-in `source-audit.json` is historical evidence, not a report for newly fetched revisions.

## Reproducibility

Record each checkout's `git rev-parse HEAD` and verify `git status --short` is clean before ingestion. Preserve the Gist cache with ingestion records because source revisions alone do not pin external examples. Keep plugin and source checkouts unchanged while queued ingestion is pending. Source corpora, caches, and generated output are excluded from Git.
