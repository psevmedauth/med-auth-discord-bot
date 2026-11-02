import requests

rss_url = "https://www.med.auth.gr/taxonomy/term/1106/feed"

r = requests.get(
    rss_url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("content-type"))
print(r.text[:2000])
