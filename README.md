# Explainedly NLWeb

NLWeb backend project for https://www.explainedly.net/.

## Goal

Expose Explainedly content through natural-language retrieval and MCP without changing Blogger hosting.

## Architecture

Blogger -> sitemap/article pages -> NLWeb -> OpenAI embeddings -> Qdrant -> /ask and /mcp

## Source

- Site: https://www.explainedly.net/
- Sitemap: https://www.explainedly.net/sitemap.xml
- Source ID: `explainedly`

## Local setup

1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Copy `.env.example` to `.env`.
5. Add `OPENAI_API_KEY` to `.env`.
6. Keep Qdrant local for development. Production should use Qdrant Cloud or another persistent deployment.

## Secrets

Never commit `.env`, OpenAI keys, Qdrant keys, hosting tokens, or other credentials.

## Deployment target

Planned public service: `nlweb.explainedly.net`.

## Status

Initial provider and source configuration is committed. The next stage is wiring the official NLWeb ingestion/server entry points, indexing the Explainedly sitemap, then testing `/ask` and `/mcp` against real articles.
