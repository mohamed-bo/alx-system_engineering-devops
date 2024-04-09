#!/usr/bin/python3
"""top_ten reddit"""
import requests


def top_ten(subreddit):
    """Reddit API returns the top 10 posts"""
    reddit = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                          .format(subreddit),
                          headers={"User-Agent": "My-User-Agent"},
                          allow_redirects=False)
    if reddit.status_code >= 300:
        print('None')
    else:
        children = reddit.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
