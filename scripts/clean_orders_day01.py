"""Week 2 · Pipeline Day 1 — local order cleanup (no cloud)."""

from __future__ import annotations

RAW_ORDERS = [
    {"order_id": 1, "user_id": "u1", "status": "completed", "amount": 120.0, "city": " hyd "},
    {"order_id": 2, "user_id": "u2", "status": "pending", "amount": 90.0, "city": "blr"},
    {"order_id": 3, "user_id": "u1", "status": "completed", "amount": None, "city": " Chennai "},
    {"order_id": 4, "user_id": "u3", "status": "completed", "amount": 55.5, "city": "blr"},
    {"order_id": 5, "user_id": "u4", "status": "cancelled", "amount": 200.0, "city": "hyd"},
    {"order_id": 6, "user_id": "u2", "status": "completed", "amount": 310.0, "city": " delhi "},
]


def main() -> None:
    cleaned = []
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