import requests
from bs4 import BeautifulSoup

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

r = requests.get(url)

print("STATUS:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

print("LINKS:", len(links))

for a in links[:20]:
    print(a.get("href"))
