import requests
from bs4 import BeautifulSoup

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

r = requests.get(url)

print("STATUS:", r.status_code)
print("ΜΗΚΟΣ HTML:", len(r.text))

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

print("ΣΥΝΟΛΟ LINKS:", len(links))

for a in links[:20\]:
    print(a.get("href"))
