# ci-demo

![CI](https://github.com/OWNER/ci-demo/actions/workflows/ci.yml/badge.svg)

A tiny Python project used to demonstrate continuous integration and
continuous deployment with GitHub Actions.

## What the pipeline does

| Job | Runs when | What it does |
| --- | --- | --- |
| `lint` | every push to `main` and every pull request | `ruff check` and `ruff format --check` |
| `test` | after `lint` passes | `pytest` with coverage on Python 3.12, 3.13 and 3.14 |
| `deploy-report` | after `test` passes, on `main` only | publishes the HTML coverage report to GitHub Pages |

## Run the same checks on your machine

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements-dev.txt

ruff check .
ruff format --check .
pytest --cov=calculator --cov-report=term-missing
```

CI is just these commands running on someone else's computer, every time
anyone pushes.
