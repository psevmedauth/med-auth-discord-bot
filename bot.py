import requests
import xml.etree.ElementTree as ET

rss_url = "https://www.med.auth.gr/taxonomy/term/1106/feed"

r = requests.get(
    rss_url,
    headers={"User-Agent": "Mozilla/5.0"}
)

root = ET.fromstring(r.content)

for item in root.findall("./channel/item")[:20]:
    title = item.find("title")
    pubdate = item.find("pubDate")
    link = item.find("link")

    print("TITLE:", title.text if title is not None else "")
    print("DATE:", pubdate.text if pubdate is not None else "")
    print("LINK:", link.text if link is not None else "")
    print("-----")
