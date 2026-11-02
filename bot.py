import requests
import xml.etree.ElementTree as ET
import os

rss_url = "https://www.med.auth.gr/taxonomy/term/1106/feed"

r = requests.get(
    rss_url,
    headers={"User-Agent": "Mozilla/5.0"}
)

root = ET.fromstring(r.content)

item = root.find("./channel/item")

title = item.find("title").text
link = item.find("link").text

requests.post(
    os.environ["DISCORD_WEBHOOK"],
    json={
        "content": f"📢 Νέα ανακοίνωση Ιατρικής ΑΠΘ\n\n**{title}**\n{link}"
    }
)

print(title)
print(link)
