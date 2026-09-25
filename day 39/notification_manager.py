import os
from pathlib import Path

from dotenv import load_dotenv
from twilio.rest import Client


BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")


class NotificationManager:

    def __init__(self):

        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_WHATSAPP_FROM")
        self.to_number = os.getenv("TWILIO_WHATSAPP_TO")

        if not self.account_sid:
            raise ValueError("TWILIO_ACCOUNT_SID not found in .env")

        if not self.auth_token:
            raise ValueError("TWILIO_AUTH_TOKEN not found in .env")

        if not self.from_number:
            raise ValueError("TWILIO_WHATSAPP_FROM not found in .env")

        if not self.to_number:
            raise ValueError("TWILIO_WHATSAPP_TO not found in .env")

        self.client = Client(
            self.account_sid,
            self.auth_token
        )

    def send_message(self, message_body):

        self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=message_body
        )

        print("WhatsApp notification sent!")