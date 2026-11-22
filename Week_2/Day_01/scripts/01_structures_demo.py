"""01_structures_demo — Python Foundations for Data Engineering.

Week 2 · Day 01 — Moving from SQL queries to Python data pipelines.

Mirrors: Week_2/Day_01/notebooks/01_structures_demo.ipynb

Run from the repo root (or this folder) with the course venv active::

    python Week_2/Day_01/scripts/01_structures_demo.py

Sections:
    0. Environment sanity check
    1. The 5 core primitives & SQL equivalents
    2. list, dict, tuple, set — day-to-day operations
    3. Comprehensions (SELECT ... WHERE in one line)
"""

from __future__ import annotations

import sys

# Notebook print strings use "→"; ensure UTF-8 on Windows consoles.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# =============================================================================
# 0. Environment Sanity Check (30 Seconds)
# =============================================================================
# Verify the active Python environment before every run
# (like picking the right DB in SQL Workbench).

py_version = sys.version.split()[0]
print(f"Python version: {py_version}")
print(f"Executable: {sys.executable}")

# =============================================================================
# 1. The 5 Core Primitives & SQL Equivalents
# =============================================================================
# | Python | Example        | SQL type   |
# | int    | 42             | BIGINT     |
# | float  | 19.99          | DOUBLE     |
# | str    | "HYD"          | VARCHAR    |
# | bool   | True / False   | BOOLEAN    |
# | None   | None           | NULL       |
#
# Traps: x = 10 assigns; x == 10 compares. Use `is None`, not `== None`.

# --- Example — Types, f-strings & None checks ---
order_id = 42
amount = 19.99
city = "HYD"
is_completed = True
discount = None

status = "completed"
log_path = f"s3://aws-de-keystone-datasets/orders/status={status}"
print(f"log_path={log_path}")
print(f"discount is missing: {discount is None}")

units_sold, unit_price = 7, 24.50
has_discount = discount is not None
revenue = units_sold * unit_price
print(f"revenue={revenue:.2f}, has_discount={has_discount}")

# =============================================================================
# 2. The 4 Data Structures (list, dict, tuple, set)
# =============================================================================
# | Structure | SQL-style mental model                          |
# | list      | Many values in order (duplicates allowed)       |
# | dict      | One full row as name → value                    |
# | tuple     | Two columns on one line — read only             |
# | set       | SELECT DISTINCT (no duplicates)                 |

# --- list: ordered, mutable batch ---
# Use [ ]. Append and edit in place—like collecting many amount values from rows.
batch = [10, 20, 20]
print(f"start           → batch = {batch}")

batch.append(30)  # add one item at the end
print(f"after append    → batch = {batch}")

batch.extend([40, 50])  # add many items at the end (like UNION ALL rows)
print(f"after extend    → batch = {batch}")

batch.insert(1, 15)  # insert at index 1; items at 1+ shift right
print(f"after insert    → batch = {batch}")

last = batch.pop()  # remove & return last item
print(f"after pop       → batch = {batch}, popped value = {last}")

batch.remove(20)  # remove first matching value (only one 20)
print(f"after remove(20)→ batch = {batch}")

batch.sort()  # sort in place (mutates the list)
print(f"after sort      → batch = {batch}")

copy = batch.copy()  # shallow copy — new list, same numbers inside
copy.append(999)
print(f"after copy+edit → batch = {batch}, copy = {copy}")

# print(f"len(batch)={len(batch)}, count(20)={batch.count(20)}, index(50)={batch.index(50)}")  # fails: 50 was popped
print(f"slice [1:3]     → {batch[1:3]}  # new list, batch unchanged")

# --- dict: one row / JSON record ---
# Use { } with keys (column names) and values. One JSON row from orders.
row = {"order_id": 101, "amount": 250.0, "status": "completed"}
print(f"start           → row = {row}")

row["city"] = "HYD"  # add / overwrite a column on this row
print(f"after row['city']→ row = {row}")

row.update({"amount": 275.0, "currency": "INR"})  # merge keys in place
print(f"after update    → row = {row}")

discount = row.get("discount", 0.0)  # COALESCE-style; row unchanged
print(f"get missing key → discount = {discount}, row = {row}")

status = row.pop("status")  # remove key and return its value
print(f"after pop       → status = {status}, row = {row}")

row.setdefault("source", "bronze")  # set only if key missing
print(f"after setdefault→ row = {row}")

print(f"keys   → {list(row.keys())}")
print(f"values → {list(row.values())}")
print(f"items  → {list(row.items())}")
print(f"'order_id' in row → {'order_id' in row}")

snapshot = row.copy()
snapshot["order_id"] = 999
print(f"copy+edit       → row = {row}, snapshot = {snapshot}")

# --- tuple: a small fixed bundle (read-only) ---
# Think of one order line: order_id and qty — like SELECT order_id, qty FROM order_items.
order_line = (101, 3)  # (order_id, qty) — one line on an order
print(f"start           → order_line = {order_line}")

order_id = order_line[0]  # first column in the pair
print(f"read [0]        → order_id = {order_id}, order_line still {order_line}")

qty = order_line[1]  # second column in the pair
print(f"read [1]        → qty = {qty}, order_line still {order_line}")

print(f"how many values → len(order_line) = {len(order_line)}")

order_id, qty = order_line  # unpack into two names; tuple unchanged
print(f"unpack          → order_id={order_id}, qty={qty}, order_line still {order_line}")

# order_line[1] = 5  # TypeError — cannot edit (use a list or dict to update qty)

# --- set: DISTINCT, membership, EXCEPT ---
# No duplicates. u2 in users is like filtering by user_id. active - churned is like EXCEPT.
users = {"u1", "u2"}
print(f"start           → users = {users}")

users.add("u3")  # add one member
print(f"after add('u3') → users = {users}")

users.add("u2")  # duplicate ignored
print(f"after add('u2') → users = {users}  # still one u2")

users.discard("u99")  # remove if present; no error if missing
users.remove("u1")  # remove or KeyError if missing
print(f"after removes   → users = {users}")

active = {"u1", "u2", "u3"}
churned = {"u3", "u4"}
print(f"union  active|churned   → {active | churned}")  # DISTINCT combine
print(f"intersect active&{{u2,u3}}→ {active & {'u2', 'u3'}}")  # INNER JOIN keys
print(f"except active-churned    → {active - churned}")  # active not in churned

tags = {"raw"}
tags.update({"curated", "raw"})  # merge in place
print(f"after update    → tags = {tags}")

print(f"u2 in active    → {'u2' in active}")

# =============================================================================
# 3. Comprehensions (SQL SELECT ... WHERE in one line)
# =============================================================================
# | Python                  | SQL pattern              |
# | [x for x in rows if cond] | SELECT x FROM rows WHERE |
# | {k: v for ...}            | Lookup map (id → column) |

ORDERS = [
    {"order_id": 10, "amount": 50.0},
    {"order_id": 11, "amount": 150.0},
    {"order_id": 12, "amount": 200.0},
]

# --- Example — filter (WHERE amount > 100) ---
big_ids = [r["order_id"] for r in ORDERS if r["amount"] > 100]
print(f"orders over 100 → big_ids = {big_ids}")

# --- Example — lookup map ---
amount_by_id = {r["order_id"]: r["amount"] for r in ORDERS}
print(f"amount_by_id → {amount_by_id}")
print(f"order 11 amount → {amount_by_id[11]}")

# --- Example — filter amounts ---
small_amounts = [r["amount"] for r in ORDERS if r["amount"] < 100]
print(f"amounts under 100 → small_amounts = {small_amounts}")