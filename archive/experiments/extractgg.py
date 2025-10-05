import os
import requests
from bs4 import BeautifulSoup

# Directory to save downloaded books
os.makedirs("data", exist_ok=True)

# Fetch the Top 100 page
top_100_url = "https://www.gutenberg.org/browse/scores/top"
response = requests.get(top_100_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the list of top 100 eBooks
top_ebooks = soup.find_all("ol")[0].find_all("li")

# Extract eBook IDs and titles
ebook_ids = []
for ebook in top_ebooks:
    link = ebook.find("a")
    if link and "/ebooks/" in link.get("href", ""):
        ebook_id = link.get("href").split("/ebooks/")[1]
        title = link.text.strip().replace(" ", "_").replace("/", "_")
        ebook_ids.append((ebook_id, title))

# Download each eBook
for ebook_id, title in ebook_ids:
    txt_url = f"https://www.gutenberg.org/files/{ebook_id}/{ebook_id}-0.txt"
    try:
        r = requests.get(txt_url)
        r.raise_for_status()
        with open(f"data/raw_data/{title}.txt", "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"✅ Downloaded: {title}")
    except Exception as e:
        print(f"❌ Failed to download {title}: {e}")
