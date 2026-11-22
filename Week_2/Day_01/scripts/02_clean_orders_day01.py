"""02_clean_orders_day01 — Bronze → Silver order cleanup (local, stdlib only).

Week 2 · Pipeline Day 1

Mirrors: Week_2/Day_01/notebooks/02_clean_orders_day01.ipynb

Scenario
--------
Six raw dict rows (`RAW_ORDERS`) simulate bronze JSON. Some rows are not
analytics-ready: non-completed status, NULL ``amount``, messy ``city`` strings.

Your job (same rules as the notebook §1)
-----------------------------------------
A. **Filter** — For each row in ``RAW_ORDERS``:

   - Skip if ``status`` is not ``"completed"`` (drops order_id 2, 5).
   - Skip if ``amount`` is ``None`` (drops order_id 3).

B. **Transform** — For each row you keep, append a copy with::

       city = row["city"].strip().upper()

   (e.g. ``" hyd "`` → ``"HYD"``). Keep all other keys unchanged.

C. **Report** — From the resulting ``cleaned`` list:

   - ``unique_users``: set of ``user_id``
   - ``total_revenue``: sum of ``amount``
   - Print summary line + sorted users (+ each row in the notebook)

Expected output when correct
-----------------------------
::

    Pipeline Day 1 | valid_orders=3 | unique_users=3 | revenue=485.50
    Users seen: ['u1', 'u2', 'u3']

Silver rows: order_id 1 (HYD), 4 (BLR), 6 (DELHI).

Run::

    python Week_2/Day_01/scripts/02_clean_orders_day01.py
"""

from __future__ import annotations

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# --- §2. Input data (bronze — do not edit) -----------------------------------
RAW_ORDERS = [
    {"order_id": 1, "user_id": "u1", "status": "completed", "amount": 120.0, "city": " hyd "},
    {"order_id": 2, "user_id": "u2", "status": "pending", "amount": 90.0, "city": "blr"},
    {"order_id": 3, "user_id": "u1", "status": "completed", "amount": None, "city": " Chennai "},
    {"order_id": 4, "user_id": "u3", "status": "completed", "amount": 55.5, "city": "blr"},
    {"order_id": 5, "user_id": "u4", "status": "cancelled", "amount": 200.0, "city": "hyd"},
    {"order_id": 6, "user_id": "u2", "status": "completed", "amount": 310.0, "city": " delhi "},
]


def main() -> None:
    # --- §3. Filter + normalize ---------------------------------------------
    cleaned: list[dict] = []
    for row in RAW_ORDERS:
        if row.get("status") != "completed":
            continue
        if row.get("amount") is None:
            continue
        normalized = {
            **row,
            "city": row["city"].strip().upper(),
        }
        cleaned.append(normalized)

    # --- §4. Metrics & report -------------------------------------------------
    unique_users = {r["user_id"] for r in cleaned}
    total_revenue = sum(r["amount"] for r in cleaned)

    print(
        f"Pipeline Day 1 | valid_orders={len(cleaned)} "
        f"| unique_users={len(unique_users)} "
        f"| revenue={total_revenue:.2f}"
    )
    print(f"Users seen: {sorted(unique_users)}")
    for r in cleaned:
        print(r)


if __name__ == "__main__":
    main()