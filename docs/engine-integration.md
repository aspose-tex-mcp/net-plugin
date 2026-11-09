# Context engine integration

Use [plugin-based ingestion](https://github.com/aspose-core-mcp/context-engine/blob/main/docs/engine-only.md) with an engine implementing `adcs.extraction.v1`. Install and configure the engine separately; it owns runtime stores, indexing, publication, and serving.

## Recommended TeX deployment

Use [aspose-tex-mcp/net-server](https://github.com/aspose-tex-mcp/net-server) for a deployment with pinned public engine and plugin revisions. Follow its [setup](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/setup.md) and [ingestion guide](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/ingestion.md). Its catalog already registers `aspose.tex.net`; no change to the shared engine's default catalog is required.

The server helpers use `engine/` as the ingestion workspace and `plugins/tex-net/` for the plugin and Gist cache. Use that guide's paths when deploying the server. The standalone instructions below use this plugin checkout as the workspace instead.

## Optional: register with an existing engine

> **Using `aspose-tex-mcp/net-server`?** Registration is already configured. Skip the manual registration steps below and follow the server's [setup](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/setup.md) and [ingestion guides](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/ingestion.md).

These steps are only for adding the plugin to an existing or custom context-engine deployment.

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

## Connect an MCP client

Follow the [TeX server client guide](https://github.com/aspose-tex-mcp/net-server/blob/main/docs/clients.md) and configure your client with your deployed `/tex/net/mcp/v1/streamable-http` endpoint. The server is self-hosted; no hosted endpoint is supplied. Ingest and publish TeX content before evaluating retrieval results.

The client guide includes generic VS Code Copilot MCP configuration. A dedicated TeX Copilot custom-agent repository is still pending publication.
