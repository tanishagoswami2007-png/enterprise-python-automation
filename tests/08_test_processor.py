from report_generator.processor import process_data

def test_process_data():
    raw = {
        "bpi": {
            "USD": {"rate": "100,000.00"},
            "EUR": {"rate": "90,000.00"},
        }
    }
    result = process_data(raw)
    assert result["asset"] == "Bitcoin"
    assert result["usd_rate"] == "100,000.00"
    assert result["eur_rate"] == "90,000.00"
