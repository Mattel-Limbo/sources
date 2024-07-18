import os
from dotenv import load_dotenv, dotenv_values
import requests

load_dotenv() 

# Send Post to Discord Webhook
def postToWebhook(body):
    url = os.getenv("DISCORD_WEBHOOK_URL")
    headers = {"Content-Type": "application/json"}  
    data = {
        "username": "Metiw Sang Pengayom",
        "embeds": [
            {
            "author": {
                "name": body.username,
                "url": "https://github.com/mattel-Limbo",
                "icon_url": body.avatar
            },
            "title": body.title,
            "url": "https://google.com/",
            "description": f"```{body.description}```",
            "color": 15258703,
            "fields": [
                {
                "name": "Tanggal",
                "value": body.timestamp,
                },
                {
                "name": "Thanks!",
                "value": "For using us!"
                }
            ],
            }
        ]
        }

    result = requests.post(url, json=data, headers=headers)

    message = "Webhook not sent" if result.status_code == 300 else "Webhook sent"

    return {
        "ok": result.ok,
        "status_code": result.status_code,
        "message": message,
        "data": data
    }