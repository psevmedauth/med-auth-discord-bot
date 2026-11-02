import requests
from bs4 import BeautifulSoup
import os

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all("a", href=True):
    href = a["href"]

    if "/article/" in href:
        title = a.get_text(strip=True)

        if title:
            link = "https://www.med.auth.gr" + href

            requests.post(
                os.environ["DISCORD_WEBHOOK"],
                json={
                    "content": f"📢 Νέα ανακοίνωση Ιατρικής ΑΠΘ\n\n**{title}**\n{link}"
                }
            )

            print("FOUND:", title)
            break
