import requests
import os

r = requests.post(
    os.environ["DISCORD_WEBHOOK"],
    json={"content": "✅ TEST από GitHub Actions"}
)

print("Status code:", r.status_code)
print("Response:", r.text)
