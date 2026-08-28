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
uv run strong_password.py --help
uv run strong_password.py -t memorable -l 5      # e.g. Stubbed Congress Tiptop Playmate Stagnate
uv run strong_password.py -t random -l 16        # e.g. aB3$cD9#eF2@gH7!
uv run strong_password.py -t random              # default length: 12
```

Options:

- `-t`, `--type` (required): `memorable` (words) or `random` (characters)
- `-l`, `--length`: number of words (memorable) or characters (random); default 12

Compare the two kinds with the [zxcvbn](https://github.com/dwolfhub/zxcvbn-python) strength estimator:

```bash
uv run compute_crack_time.py
```

## Tests

```bash
uv run pytest
```

## Files

- `strong_password.py` — the generator and its command line (`argparse`)
- `compute_crack_time.py` — strength comparison, uses the `zxcvbn` dependency
- `tests/` — pytest suite
- `data/eff_large_wordlist.txt` — the [EFF long wordlist](https://www.eff.org/dice) (7776 words)
- `pyproject.toml`, `uv.lock`, `.python-version` — the project's declared dependencies, the exact resolved versions, the pinned Python
- `.github/workflows/tests.yml` — runs the tests on every push
