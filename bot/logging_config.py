import logging
import json
from datetime import datetime, UTC


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)


def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler("trading_bot.log")
        file_handler.setLevel(logging.INFO)

        file_handler.setFormatter(JSONFormatter())

        logger.addHandler(file_handler)

    return logger