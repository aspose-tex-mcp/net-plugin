# Context engine integration

Use [plugin-based ingestion](https://github.com/aspose-core-mcp/context-engine/blob/main/docs/engine-only.md) with an engine implementing `adcs.extraction.v1`. Install and configure the engine separately; it owns runtime stores, indexing, publication, and serving.

## Register the plugin

Create a deployment-specific catalog, preserving any existing registrations:

```json
{
  "plugins": ["/absolute/path/to/tex-net-plugin/plugin.json"],
  "compositions": []
}
```

Source paths are relative to the ingestion workspace, not the catalog file. Prepare the sources and Gist cache using [source preparation](source-preparation.md), then run from the activated engine environment:

```sh
adcs-platform-ingest aspose.tex.net \
  --catalog /absolute/path/to/catalog.json \
  --workspace /absolute/path/to/tex-net-plugin \
  --python /absolute/path/to/tex-net-plugin/.venv/bin/python
```

This validates extraction and may write operation metadata. Registration does not clone sources, install dependencies, or publish indexes. After configuring runtime stores and embeddings, add `--publish` to publish content explicitly. Consult the engine guide for staging and queued ingestion options.

## Retrieval and serving

This plugin has no `retrieval_profile` field or profile file. It uses the engine's default retrieval behavior. Configure the deployment's product catalog and MCP serving according to the engine guide; installing the plugin does not dynamically create HTTP routes.

Extractor or source changes require re-extraction and publication of affected content. Restarting a server alone does not update indexed symbols or excerpts.

A dedicated public TeX server deployment repository and client setup guide are pending publication. Until then, use the [engine deployment documentation](https://github.com/aspose-core-mcp/context-engine/blob/main/DEPLOYMENT.md) and configure clients with the endpoint of your own deployment.
