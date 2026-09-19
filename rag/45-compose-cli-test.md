# Compose CLI test coverage

`tests/test_compose_cli.py` covers the local compose CLI path:

- runs `scripts/compose.py read health --verb sync`
- requires exit code 0
- parses stdout as JSON
- asserts `verb == "sync"`
- asserts `execute == false`
- asserts GARAS data is present

This is local test coverage only; it does not enable execution or any live rail.
