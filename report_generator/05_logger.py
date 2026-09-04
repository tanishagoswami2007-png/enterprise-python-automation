import logging
from pathlib import Path

def get_logger() -> logging.Logger:
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/application.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    return logging.getLogger("enterprise_report")
