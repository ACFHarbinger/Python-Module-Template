# Development Guide

## Prerequisites

- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv)
- [`just`](https://github.com/casey/just)

## Local Setup

```bash
git clone https://github.com/ACFHarbinger/Python-Module-Template.git
cd Python-Module-Template
cp .env.example .env
just setup
```

## Running Tasks

```bash
just test       # Run pytest suite
just lint       # Run ruff linter
just format     # Run ruff formatter
just typecheck  # Run mypy strict type checker
just check      # Run all quality checks
just docs       # Serve live documentation
```
