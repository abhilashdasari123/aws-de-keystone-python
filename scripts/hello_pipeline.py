"""Week 1 style — minimal data pipeline stub (KeystoneEduTech)."""

from __future__ import annotations


def main() -> None:
    rows = [{"store_id": 12, "sku": "SKU-4421", "qty": 3}]
    print(f"Loaded {len(rows)} bronze row(s) — ready for Glue later.")


if __name__ == "__main__":
    main()