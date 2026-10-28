import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

article = soup.find("a", href=lambda x: x and "/article/" in x)

if article:
    title = article.get_text(strip=True)
    link = "https://www.med.auth.gr" + article["href"]

    requests.post(
        os.environ["DISCORD_WEBHOOK"],
        json={
            "content": f"📢 Νέα ανακοίνωση Ιατρικής ΑΠΘ\n\n**{title}**\n{link}"
        }
    )
