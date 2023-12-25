import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-23&sortBy=publishedAt&apiKey=62839a3462124a86a3f7b35c360320da"
r = requests.get(url)
news = json.loads(r.text)

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print('------------------------')
