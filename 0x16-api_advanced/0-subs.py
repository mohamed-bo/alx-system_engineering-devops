#!/usr/bin/python3
"""number_of_subscribers reddit"""
import requests


def number_of_subscribers(subreddit):
    """the Reddit API returns the number of subscribers"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit),
                         headers={"User-Agent": "My-User-Agent"},
                         allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
