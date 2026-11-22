# aws-de-keystone-python

Runnable Python labs for **KeystoneEduTech AWS Data Engineering** (Week 2 — Python for pipelines).

Stdlib only for Day 1; no `pip install` required to run these scripts.

## Quick start

```powershell
cd aws-de-keystone-python
python scripts/run_all.py
```

Or run individual labs:

```powershell
python scripts/hello_pipeline.py
python scripts/structures_demo.py
python scripts/clean_orders_day01.py
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/hello_pipeline.py` | Minimal pipeline stub (Week 1 Git lab pattern) |
| `scripts/structures_demo.py` | Lists, dicts, sets, comprehensions from Day 1 |
| `scripts/clean_orders_day01.py` | Pipeline Day 1 — clean six messy orders |
| `scripts/run_all.py` | Runs every script in order for a smoke check |

## Virtual environment (recommended for Week 2+)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Later weeks may use `pandas`, `pyarrow`, and `boto3`; pin versions with `pip freeze > requirements.txt` when you add them.