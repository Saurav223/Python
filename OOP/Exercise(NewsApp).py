import requests

API_KEY = '85cb995e8f9d4b83a6659b674bcb8372'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_news(country):
    param = {
        'country': country,
        'apiKey': API_KEY
    }
    response = requests.get(BASE_URL, param=param)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch news')
        return None

def display_news(news):
    articles = news['articles']
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Description: {article['description']}")
        print(f"   URL: {article['url']}\n")

def main():
    country = input('Enter the country code (e.g., us for United States, gb for Great Britain): ')
    news = fetch_news(country)
    if news:
        display_news(news)

main()
