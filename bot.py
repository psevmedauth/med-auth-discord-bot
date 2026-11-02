import requests

r = requests.get(
    "https://www.med.auth.gr/tags/enimerosi-proptyhiakon",
    headers={"User-Agent": "Mozilla/5.0"}
)

print(r.text[:5000])
