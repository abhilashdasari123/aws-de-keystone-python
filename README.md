# aws-de-keystone-python

Runnable Python labs for **KeystoneEduTech AWS Data Engineering** (Week 2 — Python for pipelines).

Stdlib only for Day 1; no `pip install` required to run these scripts.

## Windows setup (Python, editor, PATH, venv)

### 1. Install Python

1. Download the latest **3.11+** installer from [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Run the installer.
3. On the first screen, check **Add python.exe to PATH** (important).
4. Choose **Install Now** (or **Customize** and ensure **pip** is selected).
5. Close and reopen PowerShell, then verify:

```powershell
python --version
```

You should see something like `Python 3.13.x`.

If `python` is not found, use the launcher:

```powershell
py --version
py -3 --version
```

### 2. Install Cursor or Visual Studio Code

Either editor works for these labs.

| Editor | Download |
|--------|----------|
| **Cursor** | [cursor.com/download](https://cursor.com/download) |
| **VS Code** | [code.visualstudio.com/Download](https://code.visualstudio.com/Download) |

After install:

1. Open this project folder: **File → Open Folder** → select `aws-de-keystone-python`.
2. Install the **Python** extension (Microsoft). Cursor bundles notebook support; in VS Code also install **Jupyter** if you use `.ipynb` files.

### 3. Install or fix `pip`

`pip` is included with the official Windows Python installer. Check:

```powershell
python -m pip --version
```

If that fails, bootstrap `pip`:

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

If Python itself is missing, reinstall from python.org and enable **pip** in the installer.

### 4. Add Python to environment variables (if not on PATH)

Only needed if `python` and `pip` work only with the full path, or `python` is not recognized.

1. Press **Win + R**, type `sysdm.cpl`, press Enter → **Advanced** → **Environment Variables**.
2. Under **User variables**, select **Path** → **Edit** → **New**.
3. Add the folder that contains `python.exe` (typical paths):
   - `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python3xx\`
   - `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python3xx\Scripts\`
4. Click **OK** on all dialogs, then **open a new PowerShell** window.

Verify:

```powershell
where.exe python
python --version
pip --version
```

**Optional (PowerShell 7+):** If script activation is blocked when creating a venv:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 5. Create and use a virtual environment

From the project root (recommended for Week 2+ and Jupyter):

```powershell
cd path\to\aws-de-keystone-python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Your prompt should show `(.venv)`. Deactivate later with:

```powershell
deactivate
```

Later weeks may use `pandas`, `pyarrow`, and `boto3`; pin versions with `pip freeze > requirements.txt` when you add them.

## Quick start

```powershell
cd aws-de-keystone-python
python Week_2/Day_01/scripts/01_structures_demo.py
```

Then:

```powershell
python Week_2/Day_01/scripts/02_clean_orders_day01.py
```

**Day 02** (functions, lambdas, decorators, generators) — notebooks only:

- `Week_2/Day_02/notebooks/01_functions_demo.ipynb`
- `Week_2/Day_02/notebooks/02_clean_orders_day02.ipynb`

## Week 2 · Day 01 layout

```
Week_2/Day_01/
  scripts/     # runnable .py labs (run in numbered order)
  notebooks/   # matching .ipynb files
```

| # | Script | Notebook | Purpose |
|---|--------|----------|---------|
| 01 | `scripts/01_structures_demo.py` | `notebooks/01_structures_demo.ipynb` | Lists, dicts, sets, comprehensions |
| 02 | `scripts/02_clean_orders_day01.py` | `notebooks/02_clean_orders_day01.ipynb` | Filter to `completed` + non-null `amount`, normalize `city`, print revenue KPIs (expect 3 orders, `485.50`) |

Open notebooks in Cursor/VS Code with the **Python (aws-de-keystone)** kernel when `.venv` is active.

## Week 2 · Day 02 layout

```
Week_2/Day_02/
  notebooks/   # labs live here (no scripts/ folder)
```

| # | Notebook | Purpose |
|---|----------|---------|
| 01 | `notebooks/01_functions_demo.ipynb` | Functions, `lambda` / `key=`, decorators, generators; anatomy diagrams under `notebooks/assets/` |
| 02 | `notebooks/02_clean_orders_day02.ipynb` | Same Day 01 silver rules via functions + `@log_pipeline_run` (3 orders, `485.50` revenue; top order_id **6**) |
