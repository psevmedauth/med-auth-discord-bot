raise Exception("TEST")

import requests
import os

print("START")

r = requests.post(
    os.environ["DISCORD_WEBHOOK"],
    json={
        "content": "✅ TEST από GitHub Actions"
    }
)

print("STATUS:", r.status_code)
print("TEXT:", r.text)

print("END")
