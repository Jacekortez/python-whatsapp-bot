import sys
import os
from dotenv import load_dotenv
import logging


def load_configurations(app):
    load_dotenv()
    app.config["ACCESS_TOKEN"] = os.getenv("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")
    app.config["YOUR_PHONE_NUMBER"] = os.getenv("254720811796")
    app.config["APP_ID"] = os.getenv("APP_ID")
    app.config["APP_SECRET"] = os.getenv("APP_SECRET")
    app.config["RECIPIENT_WAID"] = os.getenv("RECIPIENT_WAID")
    app.config["VERSION"] = os.getenv("V1")
    app.config["PHONE_NUMBER_ID"] = os.getenv("37.114.46.39:6160")
    app.config["VERIFY_TOKEN"] = os.getenv("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")


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
