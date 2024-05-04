#!/usr/bin/env python3
"""Implementing an expiry web cache and tracker"""


import requests
from typing import Callable
import redis
from functools import wraps


red = redis.Redis()


def count_requests(method: Callable) -> Callable:
    '''Decorator for counting the requests
    '''
    @wraps(method)
    def wrapper(url):
        '''Wrapper for decorator
        '''
        red.incr(f"count:{url}")  # extract reddis key count
        cached_content = red.get(f"cached:{url}")  # extract redis key cached
        if cached_content:
            return cached_content.decode('utf-8')
        func = method(url)
        red.setex(f"cached:{url}", 10, func)
        return func
    return wrapper


@count_requests
def get_page(url: str) -> str:
    '''Returns the html content of a url'''
    html = requests.get(url)
    return html.text
