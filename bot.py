import requests
from bs4 import BeautifulSoup

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

count = 0

for a in soup.find_all("a", href=True):
    href = a["href"]

    if "/article/" in href:
        title = a.get_text(strip=True)

        if title:
            print("TITLE:", title)
            print("URL:", href)
            print("-----")

            count += 1

        if count == 15:
            break
