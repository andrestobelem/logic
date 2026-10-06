# Repository instructions

These instructions apply to all files in this repository.

## Language

- Use English for documentation, comments, docstrings, and commit descriptions.
- Use Spanish to talk with the user unless the user requests another language.
- Follow ASD-STE100 for English technical text. Use the writing rules and the
  approved dictionary in the [official standard](https://www.asd-ste100.org/STE_downloads.html).
- Use short sentences, active voice, and direct instructions.
- Use one term for each concept in a context. Record technical terms in
  [the domain document](docs/domain.md).
- Review the text against the standard. A linter result does not prove that the
  text meets ASD-STE100.

## Domain model

- Read `docs/domain.md` before you change domain behavior.
- The domain is not defined yet. Do not infer its purpose from the name `logic`.
- Agree on the purpose, actors, use cases, examples, and rules before you add
  domain behavior. Record unresolved questions.
- Use the agreed terms in documentation, code, APIs, and tests.
- Write tests for observable rules and examples before you implement behavior.
- Add entities, value objects, and context boundaries only when the domain
  requires them. Do not add layers, repositories, or generic services in advance.
- Keep domain rules independent of external systems. Add interfaces when a use
  case requires an external system.
- When a concept changes, update its definition, code, and tests in the same
  change. If one term has different meanings, identify its context.

## Python tools

- Use Python 3.14 and `uv` for environments, dependencies, and Python commands.
- Keep `.python-version` set to `3.14` and `requires-python` set to
  `>=3.14,<3.15`.
- Use `uv add` for runtime dependencies and `uv add --dev` for development tools.
- Commit `uv.lock`. Let `uv` update it; do not edit it by hand.
- Use `uv sync --locked` to install the recorded dependencies.
- Keep the package in `src/logic` and tests in `tests`.
- Add type annotations to functions. Use Ruff for format and lint checks, pytest
  for tests, and ty for type checks.
- Before a code or tool change is complete, run:

  ```sh
  uv sync --locked
  uv run --locked ruff format --check .
  uv run --locked ruff check .
  uv run --locked ty check
  uv run --locked pytest
  uv build
  ```

- For a text-only change, review the text, links, and diff. Run code checks if the
  change affects a command or code example.
- Report checks that you cannot run. Do not report an untested check as passed.

## Commits

- Use Conventional Commits: `type(scope): description`. The scope is optional.
- Use a type such as `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `ci`.
  Mark a breaking change with `!` or a `BREAKING CHANGE:` footer.
- Write the description in English. State the change with a direct verb.
- Keep one purpose per commit. Include the related code, tests, and documents.
- Keep each commit verifiable. Do not commit a partial change that breaks the
  required checks.
- Before each commit, review the staged diff and run the relevant checks.
- Stage only files for the intended change. Do not include or discard changes
  from other work.
- Never add a `Co-authored-by` trailer, an agent attribution, or an automatic
  signature to a commit message.
