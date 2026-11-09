# Aspose.TeX for .NET extraction plugin

Documentation and API reference extraction for Aspose.TeX for .NET, implementing the `adcs.extraction.v1` worker contract. The plugin normalizes Markdown, extracts examples and API symbols, and produces chunks for the [Aspose Context Engine](https://github.com/aspose-core-mcp/context-engine).

Extraction uses the Python standard library and has no engine or Words runtime dependency. This plugin has **no retrieval profile**; the engine's default retrieval behavior applies. Product identity is `aspose.tex`; API namespace spelling such as `Aspose.TeX.IO` is preserved.

## Project family

| Repository | Responsibility |
| --- | --- |
| [context-engine](https://github.com/aspose-core-mcp/context-engine) | Shared ingestion, indexing, retrieval, and MCP infrastructure |
| [net-plugin](https://github.com/aspose-tex-mcp/net-plugin) **(this repository)** | TeX/.NET documentation and API extraction |
| [net-server](https://github.com/aspose-tex-mcp/net-server) | Deployment helpers combining pinned engine and TeX plugin versions |
| [docs](https://github.com/aspose-tex-mcp/docs) | Documentation source Markdown |
| [reference](https://github.com/aspose-tex-mcp/reference) | API reference source Markdown |

Use the [TeX server setup guide](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/setup.md) to deploy the engine with this plugin registered, then follow [client setup](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/clients.md). A dedicated TeX Copilot custom-agent repository is still pending publication.

## Quick start

Requires Python 3.12 or newer. From this repository root:

```sh
python3.12 -m venv .venv
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -I worker.py < examples/extract-request.json
```

The example runs offline against inline Markdown. It demonstrates extraction without installing the engine or downloading a corpus. See the [worker contract](docs/worker-contract.md) for discovery and extraction requests.

Use a source checkout for deployment: the manifest, source fixtures, and prepared Gist cache are not included in the Python wheel. An installed package exposes `adcs-tex-net-extract` and `python -I -m adcs_tex_net.worker`.

## Prepare and ingest content

1. Follow [source preparation](docs/source-preparation.md) to clone the documentation and API repositories and prepare referenced Gist examples.
2. Register the plugin with the engine using the [integration guide](docs/engine-integration.md).
3. Validate extraction, configure runtime stores, and publish indexed content explicitly.

The plugin does not launch an MCP server or publish data on its own. Source configuration is authoritative in `plugin.json`; citations use `docs.aspose.com/tex/net` and `reference.aspose.com/tex/net`.

## Validation

GitHub Actions runs the offline regression suite and extraction example on Python 3.12 and 3.13. See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks.

The historical [source audit](docs/source-audit.json) records extraction of 48 documentation pages and 325 API pages at the revisions recorded there. It predates this repository's source URL migration and does not establish current corpus coverage or deployed retrieval quality. Rerun the audit against prepared sources as described in the source preparation guide.

## License and provenance

[MIT License](LICENSE). Derived from the [Words/.NET extraction plugin](https://github.com/aspose-words-mcp/net-plugin), with the original copyright notice preserved. Fixture origins and revisions are documented in [tests/fixtures/README.md](tests/fixtures/README.md).
