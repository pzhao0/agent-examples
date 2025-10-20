import os
import json
import requests
import sys
from fastmcp import FastMCP
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=os.getenv("LOG_LEVEL", "DEBUG"), stream=sys.stdout, format='%(levelname)s: %(message)s')

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

mcp = FastMCP("Movie Review")

@mcp.tool(annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True})
def get_plot(movie_title: str) -> str:
    """Get the plot summary of a movie from OMDb API."""
    base_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&"
    params = {"t": movie_title, "plot": "full"}
    response = requests.get(base_url, params=params, timeout=10)
    data = response.json()
    if "Plot" in data:
        return data["Plot"]
    return "Movie not found"

@mcp.tool(annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True})
def get_movie_details(movie_title: str) -> str:
    """Get full details (awards, actors, plot, and reviews, etc.) of a movie from OMDb API."""
    base_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&"
    params = {"t": movie_title, "plot": "full"}
    response = requests.get(base_url, params=params, timeout=10)
    data = response.json()
    if data["Response"] == "True":
        del data["Response"]
        del data["Poster"]
        return json.dumps(data)
    return "Movie not found"

# host can be specified with HOST env variable
# transport can be specified with MCP_TRANSPORT env variable (defaults to streamable-http)
def run_server():
    "Run the MCP server"
    transport = os.getenv("MCP_TRANSPORT", "streamable-http")
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    mcp.run(transport=transport, host=host, port=port)

if __name__ == "__main__":
    if OMDB_API_KEY is None:
        logger.warning("Please configure the OMDB_API_KEY environment variable before running the server")
    run_server()
