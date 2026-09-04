from pathlib import Path
from report_generator.pdf_generator import generate_pdf

def test_generate_pdf(tmp_path):
    data = {
        "report_time": "2026-09-04 00:00:00 UTC",
        "asset": "Bitcoin",
        "usd_rate": "100,000.00",
        "eur_rate": "90,000.00",
        "source": "Test source",
    }
    output = generate_pdf(data, str(tmp_path))
    assert Path(output).exists()
    assert Path(output).stat().st_size > 0
