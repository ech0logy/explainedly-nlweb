"""Run the Explainedly NLWeb HTTP and MCP server."""

import os

from nlweb_network import NLWebServer


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    server = NLWebServer(config_path="config/config.yaml")
    server.run(host=host, port=port)
