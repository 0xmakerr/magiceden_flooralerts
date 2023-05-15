import requests
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://api-mainnet.magiceden.dev/v2/collections/pyth_alligators/stats"  # Include the scheme here

payload = {}
headers = {}

while True:
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    floor = int(json_response["floorPrice"] / 1e9)
    if floor < 59:
        webhook = DiscordWebhook(url='YOUR WEBHOOK', content=f'@here Pyth Gator FP: {str(floor)}')
        response = webhook.execute()
    time.sleep(2)