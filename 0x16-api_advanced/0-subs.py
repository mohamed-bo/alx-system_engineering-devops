#!/usr/bin/python3
"""number_of_subscribers reddit"""
import requests


def number_of_subscribers(subreddit):
    """the Reddit API returns the number of subscribers"""
    import requests

    reddi = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit),
                         headers={"User-Agent": "My-User-Agent"},
                         allow_redirects=False)
    if reddi.status_code >= 300:
        return 0
    return reddi.json().get("data").get("subscribers")
