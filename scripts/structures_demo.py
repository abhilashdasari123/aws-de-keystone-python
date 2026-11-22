"""Week 2 Day 1 — core structures and comprehensions (stdlib demo)."""

from __future__ import annotations

ORDERS = [
    {"order_id": 10, "amount": 50.0},
    {"order_id": 11, "amount": 150.0},
    {"order_id": 12, "amount": 200.0},
]


def demo_primitives() -> None:
    qty = 12
    unit_price = 19.99
    line_total = qty * unit_price
    print(f"primitives | line_total={line_total:.2f}")


def demo_collections() -> None:
    amounts = [10, 20, 20]
    amounts.append(30)
    row = {"order_id": 101, "amount": 250.0}
    discount = row.get("discount", 0.0)
    paid_users = {"u1", "u2", "u2"}
    print(
        f"collections | amounts_len={len(amounts)} "
        f"| discount_default={discount} | unique_users={len(paid_users)}"
    )


def demo_comprehensions() -> None:
    big_ids = [r["order_id"] for r in ORDERS if r["amount"] > 100]
    amount_by_id = {r["order_id"]: r["amount"] for r in ORDERS}
    print(f"comprehensions | big_ids={big_ids} | amount_by_id={amount_by_id}")


def main() -> None:
    demo_primitives()
    demo_collections()
    demo_comprehensions()


if __name__ == "__main__":
    main()