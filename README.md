# Donna Backend

Production-grade FastAPI backend for Donna, an AI executive assistant.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env

alembic upgrade head
uvicorn donna.main:app --reload
```

Health check:

```bash
curl http://localhost:8000/health
```

Open API docs:

```text
http://localhost:8000/docs
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

Core principle:

> Donna is not a chatbot. Donna is a safe action system with an LLM interface.