# Jarvis

A personal assistant for the terminal, written in Python. It chats through an OpenAI-compatible API and can call local tools to read files, folders and PDFs inside your home directory.

**Status:** work in progress. The list below is what works today.

## What works today

- **Chat in the terminal.** Replies are rendered as Markdown with Rich.
- **Tool calling.** The model can call five local functions, with up to six tool rounds per message:

  | Tool | What it does |
  |---|---|
  | `get_time_date` | Returns the current date and time |
  | `get_home_directory` | Returns the path of the home directory |
  | `get_folder_data` | Lists the visible contents of a folder |
  | `get_file_data` | Reads a text file |
  | `get_pdf_data` | Converts a PDF to Markdown with `pymupdf4llm` |

- **A guard on file access.** A path outside the home directory, or one with a hidden part such as `.ssh`, is refused with `Out of Bounds`.
- **A configurable personality.** The system prompt is assembled from the Markdown files in `assets/prompts`, in file-name order. Edit, add or remove a file to change how the assistant behaves.
- **Conversation memory.** The conversation is saved to `conversation.json` and loaded again on the next start.
- **Error handling.** API errors are logged with Loguru to `logs/` and the assistant answers with a short fallback line.

## Stack

Python, the OpenAI Python SDK (pointed at OpenRouter), Typer, Rich, Pydantic Settings, Loguru, PyMuPDF4LLM, pytest, ruff and mypy.

## Run it

```bash
git clone https://github.com/MoeedSarwar1/Jarvis.git
cd Jarvis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```
OPENROUTER_API_KEY=your-key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
AI_MODEL=the-model-you-want-to-use
```

Then start the assistant:

```bash
python main.py
```

Type `exit`, `quit` or `shutdown` to stop.

## Tests

```bash
pytest
```

The tests cover the tools, the file-access guard and the chat function with a mocked API client.

## Project layout

```
main.py            entry point (Typer)
core/              client, conversation loop, tools, personality loader
config/            settings, logger, constants
assets/prompts/    the Markdown files that make up the system prompt
tests/             pytest tests
```
