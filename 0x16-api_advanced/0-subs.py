#!/usr/bin/python3
"""function that queries the Reddit API"""
import json
import requests


def number_of_subscribers(subreddit):
    """fetches number of subscribers in a subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.reddit.com/r/{subreddit}/about.json')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'subscribers' in data['data']:
            return (data['data']['subscribers'])
        else:
            return (0)
    else:
        return (0)
