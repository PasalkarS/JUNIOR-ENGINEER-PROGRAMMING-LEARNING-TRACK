"""
Reporting and summary calculations.
"""
def calculate_expense_summary(expenses: list[dict]) -> dict:
    total = sum(e["amount"] for e in expenses)
    by_category = {}
    by_month = {}
    for e in expenses:
        cat = e["category"]
        amt = e["amount"]
        month = e["date"][:7] if len(e["date"]) >= 7 else "Unknown"

        by_category[cat] = by_category.get(cat, 0.0) + amt
        by_month[month] = by_month.get(month, 0.0) + amt

    return {
        "total_expenses": round(total, 2),
        "by_category": {k: round(v, 2) for k, v in by_category.items()},
        "by_month": {k: round(v, 2) for k, v in by_month.items()},
    }

def calculate_asset_summary(assets: list[dict]) -> dict:
    total = sum(a["value"] for a in assets)
    by_category = {}
    for a in assets:
        cat = a["category"]
        val = a["value"]
        by_category[cat] = by_category.get(cat, 0.0) + val

    return {
        "total_asset_value": round(total, 2),
        "by_category": {k: round(v, 2) for k, v in by_category.items()},
    }

def calculate_net_worth_overview(expenses: list[dict], assets: list[dict]) -> dict:
    exp_summary = calculate_expense_summary(expenses)
    ast_summary = calculate_asset_summary(assets)
    net_worth = ast_summary["total_asset_value"] - exp_summary["total_expenses"]
    return {
        "total_assets": ast_summary["total_asset_value"],
        "total_expenses": exp_summary["total_expenses"],
        "net_balance": round(net_worth, 2),
    }
