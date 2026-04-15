import requests 
import threading
import time
import os
from dotenv import load_dotenv

load_dotenv()

COOKIES = os.getenv("COOKIES")


def trace(func):
    def inner(*args):
        tag = args[1].get('type')
        print(f"{time.perf_counter():.3f} [{threading.current_thread().name}] {tag}")
        return func(*args)
    return inner

def get_cookies_dict(cookie_string):
    """Parses cookie string into a dictionary."""
    cookies = {}
    for item in cookie_string.split(';'):
        if '=' in item:
            name, value = item.split('=', 1)
            cookies[name.strip()] = value.strip()
    return cookies

def get_headers():
    return {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8',
    'priority': 'u=1, i',
    'referer': 'https://www.educative.io/',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-ed-client': 'v260109-h-260118-1410'
}
    
_thread_local = threading.local()
    
def get_session():
    if not hasattr(_thread_local,'session'):
        cookies = get_cookies_dict(COOKIES)
        session = requests.Session()
        session.cookies.update(cookies)
        _thread_local.session = session 
    return _thread_local.session 
