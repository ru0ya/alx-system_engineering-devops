#!/usr/bin/python3
"""function that queries Reddit API"""

import requests
import json


def top_ten(subreddit):
    """gets the top ten post in a subreddit"""
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
