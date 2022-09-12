from nntplib import ArticleInfo
from operator import getitem, itemgetter
import requests
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

results = requests.get(url)
results_json = results.json()
article_dicts = []
for result in results_json[:5]:
    articles = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{result}.json")
    article_json = articles.json()
    
    article_dict = {
        'title' : article_json['title'],
        'link' : f"https://hacker-news.firebaseio.com/v0/item/{article_json['id']}.json",
        'comments' : article_json['descendants'],
    }
    article_dicts.append(article_dict)


article_dicts = sorted(article_dicts, reverse= True, key= itemgetter('comments'))

for sorted_art in article_dicts :
    print(f"\nTitle : {sorted_art['title']}")
    print(f"Link : {sorted_art['link']}")
    print(f"Comment count : {sorted_art['comments']}")