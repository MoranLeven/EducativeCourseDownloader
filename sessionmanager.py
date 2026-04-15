# this is a session manager class
import requests
import threading
import os
from dotenv import load_dotenv

load_dotenv()

class SessionManager:
    COOKIES = os.getenv("COOKIES")
    _thread_local = threading.local()

    def __init__(self):
        self.session = None
        self.threaded_session = None
        self.headers = self.headers()
        self.cookie = self.get_cookies_dict(SessionManager.COOKIES)

    def headers(self):
        return {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,de;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.educative.io",
            "priority": "u=1, i",
            "referer": "https://www.educative.io/search?tab=courses&query=System%20Design",
            "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
            "x-ed-client": "v260123-h-260127-1246",
        }

    def start_session(self):
        session = requests.Session()
        session.cookies.update(self.cookie)
        self.session = session
        return session

    def start_threaded_session(self):
        session = requests.Session()
        session.cookies.update(self.cookie)
        self.threaded_session = session
        SessionManager._thread_local.session = session
        return session

    def get_cookies_dict(self, cookies):
        cookie = {}
        for item in cookies.split(";"):
            if "=" in item and item.count("=") == 1:
                name, value = item.split("=")
                cookie[name.strip()] = value.strip()
        return cookie
