import requests


class DiscordService:

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_shiny_found(self):

        payload = {
            "content": "@everyone Shiny encontrado!"
        }

        requests.post(
            self.webhook_url,
            json=payload,
            timeout=10
        )