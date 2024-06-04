#!/usr/bin/python3
"""
prints top ten
"""

import re
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Reddit API and returns hot posts of the subreddit"""
    reddi = requests.get("https://www.reddit.com/r/{}/hot.json"
                         .format(subreddit),
                         params={"count": count, "after": after},
                         headers={"User-Agent": "My-User-Agent"},
                         allow_redirects=False)
    if reddi.status_code >= 400:
        return None
    newHotli = hot_list + [child.get("data").get("title")
                           for child in reddi.json()
                           .get("data")
                           .get("children")]
    redditjson = reddi.json()
    if not redditjson.get("data").get("after"):
        return newHotli
    return recurse(subreddit, newHotli, redditjson.get("data").get("count"),
                   redditjson.get("data").get("after"))
