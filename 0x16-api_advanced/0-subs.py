#!/usr/bin/python3
"""number_of_subscribers reddit"""
import requests


def number_of_subscribers(subreddit):
    """the Reddit API returns the number of subscribers"""
    import requests
    try:
        headers = requests.utils.default_headers()
        headers.update({'User-Agent': 'My User Agent 1.0'})
        reddi = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers=headers,
                            allow_redirects=False)
        if reddi.status_code >= 300:
            return 0
        return reddi.json().get("data").get("subscribers")
    except requests.RequestException:
        return 0
