# password-generator

A small command-line tool that generates strong passwords — either **memorable** (random English words) or **random** (mixed characters). Exercise material for [Session 2](https://knuxv.github.io/cours-agents/sessions/s2/) of *Advanced Programming for Economists*.

## Install

You need [`uv`](https://docs.astral.sh/uv/) (Session 2, section 3). Then:

```bash
git clone https://github.com/YOUR-USERNAME/password-generator.git
cd password-generator
uv sync
```

`uv sync` reads `.python-version` and `uv.lock`, fetches Python 3.12 if needed, and builds `.venv` with the exact versions listed in the lockfile. That is the whole installation.

## Use

```bash
uv run strong_password.py        # e.g. Stubbed Congress Tiptop Playmate Stagnate
```

It takes no options yet. The two settings — which kind of password, and how long —
are written inside `main()`, at the bottom of `strong_password.py`:

```python
password_type = "memorable"  # "memorable" or "random"
length = 12
```

To get a different password you edit those lines and run the script again.

**That is the exercise:** turn them into command-line options, so that
`uv run strong_password.py -t random -l 16` works and `--help` documents itself.
The statement is on the course site, [exercise 2.3](https://knuxv.github.io/cours-agents/exercises/password-generator/).
The finished version is on the `solution` branch — look at it after you have tried.

Compare the two kinds with the [zxcvbn](https://github.com/dwolfhub/zxcvbn-python) strength estimator:

```bash
uv run compute_crack_time.py
```

## Tests

```bash
uv run pytest
```

## Files

- `strong_password.py` — the generator; its command line is yours to write
- `compute_crack_time.py` — strength comparison, uses the `zxcvbn` dependency
- `tests/` — pytest suite
- `data/eff_large_wordlist.txt` — the [EFF long wordlist](https://www.eff.org/dice) (7776 words)
- `pyproject.toml`, `uv.lock`, `.python-version` — the project's declared dependencies, the exact resolved versions, the pinned Python
- `.github/workflows/tests.yml` — runs the tests on every push
