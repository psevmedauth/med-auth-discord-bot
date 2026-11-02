import requests
from bs4 import BeautifulSoup

url = "https://www.med.auth.gr/tags/enimerosi-proptyhiakon"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=30)

print("STATUS:", r.status_code)
print(r.text[:500])
