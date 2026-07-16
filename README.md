## This would be Jarvis, My Very Own First Project In Python and Local Ai Assistant

## Personal AI Assistant — System Design

## 1. Goal & Scope

Build a modular, tool-using AI assistant, starting text-only, expanding to voice, expanding to real-world actions (calendar, files, smart home, Mac control). Each stage is a fully working product on its own — not a demo you abandon.

Non-goals (for now): training/fine-tuning models, building your own STT/TTS, multi-user support, mobile app wrapper. All of that is post-v1.

---

## 2. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Input Layer                          │
│  Text (CLI/stdin)  |  Voice (mic → STT)  |  (later) HTTP API │
└───────────────────────────┬───────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Orchestrator (core.py)                  │
│  - Builds request: system prompt + history + tool schemas   │
│  - Calls LLM (Claude API)                                   │
│  - Detects tool_use blocks in response                      │
│  - Loop: execute tool → feed result back → repeat until     │
│    LLM returns final text                                   │
└───────────────────────────┬───────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                        Tool Registry                        │
│  weather.py | calendar.py | files.py | mac_control.py |     │
│  home_assistant.py | web_search.py                          │
│  Each tool = 1 function + 1 JSON schema, registered in a    │
│  dict {name: {fn, schema}}                                  │
└───────────────────────────┬───────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Memory / State                         │
│  - Short-term: in-memory conversation list (per session)    │
│  - Long-term: SQLite (facts, preferences, past summaries)   │
└───────────────────────────┬───────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                       Output Layer                          │
│  Text (print)  |  Voice (TTS)  |  (later) push notification │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Component Breakdown

### 3.1 Orchestrator (`core.py`)

The brain loop. Responsibilities:

- Maintain conversation state (list of messages)
- Send request to Claude API with `tools` param
- Parse response: if `stop_reason == "tool_use"`, extract tool name + input, call it, append `tool_result`, re-call API
- Repeat until final text response
- Single responsibility: **orchestration only** — no tool logic lives here

### 3.2 Tool Registry (`tools/`)

One file per tool. Each exposes:

```python
SCHEMA = {
    "name": "get_weather",
    "description": "Get current weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {"location": {"type": "string"}},
        "required": ["location"]
    }
}

def execute(location: str) -> str:
    ...
```

`core.py` auto-discovers tools from this folder — adding a new capability = adding one file, zero changes to orchestrator.

### 3.3 Memory

- **Session memory**: plain Python list, lives only during the run — good enough for v1.
- **Persistent memory**: SQLite table `memories(id, content, created_at, tags)`. Written to explicitly (e.g. a `remember_this` tool) rather than auto-logging everything — keeps it useful instead of noisy.
- Do NOT try to build vector-search/RAG memory yet. Premature for a personal assistant with a few hundred facts — a simple keyword or tag lookup is enough until it visibly isn't.

### 3.4 Input/Output adapters

Keep these swappable — orchestrator shouldn't know if input came from text or voice.

```
input_adapter.get_input() -> str
output_adapter.respond(text: str) -> None
```

Text adapter: `input()` / `print()`.
Voice adapter (Stage 3+): mic capture → Whisper → same interface; TTS on the way out.

---

## 4. Build Order (Milestones)

| Stage            | Deliverable                                                                  | New concepts                              |
| ---------------- | ---------------------------------------------------------------------------- | ----------------------------------------- |
| **0**            | Repo scaffold, `.env` for API key, basic Claude API call, no tools           | API auth, env vars                        |
| **1**            | Orchestrator + 2 tools (weather, time), text-only loop                       | Tool use / function calling, JSON schemas |
| **2**            | Add file tool (read/write local files), add SQLite memory                    | File I/O, SQLite basics                   |
| **3**            | Add voice I/O (Whisper local STT + `say` or ElevenLabs TTS)                  | Audio I/O, subprocess                     |
| **4**            | Add calendar tool (Google Calendar API or macOS EventKit via `osascript`)    | OAuth or AppleScript bridging             |
| **5**            | Add Mac control tool (open apps, run shortcuts via `osascript`/`subprocess`) | System automation                         |
| **6**            | Add Home Assistant tool (REST API) if you have smart home devices            | REST integration                          |
| **7** (optional) | Wake-word always-on daemon                                                   | Background processes, `porcupine`         |

Each stage = 3-7 days at your pace (3-4 sessions/week). Don't start Stage N+1 until Stage N actually works end-to-end.

---

## 5. Repo Structure

```
jarvis/
├── .env                    # API keys, gitignored
├── requirements.txt
├── core.py                 # orchestrator loop
├── config.py                # system prompt, model name, constants
├── memory/
│   ├── db.py                 # SQLite setup + helpers
│   └── memory.db
├── tools/
│   ├── __init__.py            # auto-discovery/registry
│   ├── weather.py
│   ├── time_tool.py
│   ├── files.py
│   ├── calendar_tool.py
│   └── mac_control.py
├── io/
│   ├── text_adapter.py
│   └── voice_adapter.py       # Stage 3+
└── main.py                    # entrypoint, picks adapter, runs loop
```

---

## 6. Key Design Decisions (and why)

- **Tool-calling via Claude's native `tools` API**, not manual regex/prompt parsing — this is the actual FDE-relevant skill and far more reliable.
- **Tools are pure functions with explicit schemas** — testable in isolation, no hidden state, easy to demo individually.
- **Orchestrator has zero domain logic** — it only loops API ↔ tool execution. This keeps it stable while tools grow to 20+.
- **SQLite over a vector DB** — you don't have a retrieval problem yet (a few hundred facts fit in a `WHERE tag = ?` query). Add embeddings only when keyword lookup demonstrably fails.
- **Local Whisper over cloud STT initially** — no API cost/latency while you're iterating, swap later if quality matters.
- **`osascript`/AppleScript for Mac control** — no need for a native app; shell out from Python, same pattern as any "tool."

---

## 7. What This Teaches You (mapped to FDE skills)

- Tool/function-calling with LLM APIs — the single most important FDE skill
- API integration patterns (auth, retries, error handling)
- Structuring a codebase so new capabilities are additive, not invasive
- Bridging AI output to real-world side effects (files, calendar, system) — literally what "forward deployed" means: making AI actually do something in someone's existing environment

---

## 8. Immediate Next Action

Build Stage 0 + 1 this week:

1. Scaffold the repo structure above
2. Get a bare API call working (no tools)
3. Add `get_weather` and `get_time` tools, wire up the tool-use loop

Ask me for the Stage 0+1 starter code when ready — it's about 100 lines total.## What it would Do
