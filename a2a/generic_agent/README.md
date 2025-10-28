# Generic Agent

## Introduction

A flexible A2A agent that can be configured with multiple MCP servers to provide various capabilities. The agent dynamically loads tools from connected MCP servers and uses an LLM to orchestrate tool calls based on user requests.

## Features

- **Multi-MCP Support**: Connect to multiple MCP servers simultaneously
- **Dynamic Tool Loading**: Automatically discovers and uses tools from connected MCP servers
- **LLM Agnostic**: Works with any OpenAI-compatible API (Ollama, OpenAI, etc.)
- **A2A Protocol**: Full integration with A2A server for task management and streaming

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URLS` | Comma-separated list of MCP server URLs | `http://localhost:8000/mcp` |
| `MCP_TRANSPORT` | Transport protocol for MCP | `streamable_http` |
| `LLM_MODEL` | Model name to use | `llama3.2:3b-instruct-fp16` |
| `LLM_API_BASE` | Base URL for LLM API | `http://localhost:11434/v1` |
| `LLM_API_KEY` | API key for LLM service | `dummy` |

## Running in Kagenti

When deploying in the Kagenti UI:

1. Import your intended tools using the `Import New Tools` section.
2. In the `Import New Agent` section:
  - Choose the `ollama` or `openai` environmental variable set
  - Create a new variable, `MCP_URLS`, and add the list of MCP server URLs separated with commas. For example, if using the weather-tool and movie-tool examples, `MCP_URLS`="http://weather-tool:8000/mcp,http://movie-tool:8000/mcp"

