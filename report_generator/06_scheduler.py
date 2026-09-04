import time
import schedule
from .api import fetch_bitcoin_data
from .processor import process_data
from .pdf_generator import generate_pdf
from .logger import get_logger

logger = get_logger()

def generate_report() -> None:
    """Run the complete report-generation pipeline."""
    try:
        logger.info("Starting automated report generation")
        raw = fetch_bitcoin_data()
        processed = process_data(raw)
        path = generate_pdf(processed)
        logger.info("Report generated successfully: %s", path)
        print(f"Report generated successfully: {path}")
    except Exception as exc:
        logger.exception("Report generation failed")
        print(f"Report generation failed: {exc}")

def run_scheduler(interval_minutes: int = 60) -> None:
    """Schedule report generation repeatedly."""
    schedule.every(interval_minutes).minutes.do(generate_report)
    print(f"Scheduler started. Reports will run every {interval_minutes} minutes.")
    generate_report()

    while True:
        schedule.run_pending()
        time.sleep(1)
