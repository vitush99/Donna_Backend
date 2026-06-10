# Donna Backend

Production-grade FastAPI backend for Donna, an AI executive assistant.

## Phase A

Phase A provides an in-memory task API. Tasks are lost when the server restarts. No database, authentication, or external integrations are required.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
uvicorn donna.main:app --reload
```

The API runs at `http://localhost:8000`.

OpenAPI documentation is available at:

```text
http://localhost:8000/docs
```

## Run tests

```bash
python -m pytest
```

## Endpoints

- `GET /health`
- `POST /api/tasks`
- `GET /api/tasks`
- `GET /api/tasks/{id}`
- `PATCH /api/tasks/{id}`

## Manual testing

Check server health:

```bash
curl http://localhost:8000/health
```

Create a task:

```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Finish Phase A","description":"Complete the task API"}'
```

List all tasks:

```bash
curl http://localhost:8000/api/tasks
```

Get one task by replacing `TASK_ID` with the ID returned when the task was created:

```bash
curl http://localhost:8000/api/tasks/TASK_ID
```

Update a task:

```bash
curl -X PATCH http://localhost:8000/api/tasks/TASK_ID \
  -H "Content-Type: application/json" \
  -d '{"status":"completed"}'
```

## Architecture

This is a modular monolith:

```text
src/donna/
  api/             API routers and dependencies
  core/            config, logging, errors, security
  db/              SQLAlchemy sessions/base/transactions
  domains/         product domains: tasks, approvals, audit, users
  integrations/    external vendors: Google, OpenAI, Anthropic, Twilio, Notion
  ai/              agents, tools, prompts, memory, evals
  jobs/            background workers/schedulers
```

The database, integrations, AI, and jobs folders are future scaffolding and are not active
in Phase A.

Core principle:

> Donna is not a chatbot. Donna is a safe action system with an LLM interface.
