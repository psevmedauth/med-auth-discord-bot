import requests
from bs4 import BeautifulSoup

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

for h2 in soup.find_all(["h2", "h3"]):
    text = h2.get_text(" ", strip=True)

    if text:
        print(text)
