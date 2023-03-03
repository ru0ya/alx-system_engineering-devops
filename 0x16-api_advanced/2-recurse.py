#!/usr/bin/python3

"""
function to recrsively query a reddit api
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function return's None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')

    children = data.get('children')
    for child in children:
        title = child.get('data').get('title')
        hot_list.append(title)

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
