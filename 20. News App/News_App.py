import requests
import json

query = input("Enter the type of news you want: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-10&sortBy=publishedAt&apiKey=a96a7233b546404796e221c4af2ba7ff"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(
        "------------------------------------------------------------------------------------------------------------------"
    )
