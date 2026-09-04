from datetime import datetime, timezone

def process_data(raw: dict) -> dict:
    """Convert API response into a small report-friendly structure."""
    bpi = raw.get("bpi", {})
    usd = bpi.get("USD", {})
    eur = bpi.get("EUR", {})

    return {
        "report_time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "asset": "Bitcoin",
        "usd_rate": usd.get("rate", "N/A"),
        "eur_rate": eur.get("rate", "N/A"),
        "source": "CoinDesk public API",
    }
