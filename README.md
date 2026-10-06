# logic

This repository contains a Python package. Its domain is not defined yet.
It has no command-line interface or domain API.

## Install

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run
these commands from the repository root:

```sh
uv python install 3.14
uv sync --locked
```

The project uses Python 3.14. `uv sync --locked` creates `.venv` and installs the
package and development tools from `uv.lock`. Commit the lockfile when
dependencies change. Do not edit it by hand.

## Check

Run all checks before you commit a code or tool change:

```sh
uv sync --locked
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked ty check
uv run --locked pytest
uv build
```

Ruff checks format and lint rules. ty checks types. pytest checks behavior.
`uv build` creates a wheel and source archive in `dist/`.

To apply the code format, run `uv run --locked ruff format .`.

## Repository guides

- [Agent instructions](AGENTS.md): language, tools, checks, and commit rules.
- [Domain discovery](docs/domain.md): purpose, terms, rules, and open questions.

Use the same domain terms in documentation, code, APIs, and tests. Agree on
examples and rules before you add domain behavior.

Write repository text in English and follow
[ASD-STE100](https://www.asd-ste100.org/STE_downloads.html). Use Conventional
Commits and keep each commit to one purpose. Never add agent attributions or
`Co-authored-by` trailers.
