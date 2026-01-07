# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project overview
- Minimal Python app with a single entry point `main.py`.
- Python version pinned to 3.14 via `.python-version` and `pyproject.toml` (`requires-python = ">=3.14"`).
- No third-party dependencies, tests, or packaging/build system configured.

## Commands

### Run the app
```sh
python3 main.py
```

### Linting (syntax check only)
No linter is configured. For a quick built-in syntax check across the repo:
```sh
python3 -m compileall -q .
```

### Tests
No test framework is configured.
- If you add stdlib `unittest`, common invocations are:
```sh
# Discover and run all tests
python3 -m unittest -v

# Run a single test
python3 -m unittest tests.test_example.TestExample.test_something
```
- If you add `pytest` (not present here), common invocations are:
```sh
# Run all tests quietly
pytest -q

# Run a single test function
pytest tests/test_example.py::TestExample::test_something -q
```

### Build/package
`pyproject.toml` does not define a `[build-system]`, so building wheels/sdists is not set up. Add a build backend (e.g., Hatchling or Setuptools) before using:
```sh
python3 -m build
```

## Repository structure and architecture
- `main.py` defines a `main()` function and uses the `if __name__ == "__main__"` guard to run it. There is no package/module layout yet.
- `pyproject.toml` contains only project metadata; it does not configure dependencies, tools, or a build backend.
- `README.md` is currently empty.
- `.gitignore` excludes standard Python artifacts (e.g., `__pycache__/`, `*.py[oc]`, `build/`, `dist/`, `.venv`).

## Notes for future agents
- Honor the Python version requirement (3.14). If you need broader runtime support, coordinate changes to both `.python-version` and `pyproject.toml`.
- Before introducing lint/test/build commands into automation, add and commit the corresponding tool configurations to the repo to make them canonical.
