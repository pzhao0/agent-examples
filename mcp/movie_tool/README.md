# OMDb Movie MCP Server

This is a simple Movie MCP Server with two tools:

- `get_plot`: get full plot of a movie by name
- `get_movie_details`: get full details of a movie by name, including reviews, awards, actors, etc.

You can configure the server with the following environment variables:

| Variable name            | Required? | Default                | Description |
| ------------------------ | --------- | ---------------------- | ----------------------------- |
| `OMDB_API_KEY`           | Yes       | - | API Key for accessing the OMDB API. Required for any functionality |
| `LOG_LEVEL`              | No        | `DEBUG`                | Application log level |
| `MCP_TRANSPORT`          | No        | `streamable-http`      | Passed into mcp.run to determine mcp transport |

You can run this locally with `uv run movie_tool.py` so long as the `OMDB_API_KEY` is set. 