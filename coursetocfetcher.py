
import json
from .utilities import *
from collections import defaultdict


class CourseTOCFetcher:
    
    BASE_URL = "https://www.educative.io/api/collection/{}?work_type=collection"
    
    def __init__(self):
        self.kursos_toc = defaultdict(dict)
        
    
    def get_kurso_toc(self, kurso_name):
        #return from the cache if already exists
        if kurso_name in self.kursos_toc:
            return self.kursos_toc[kurso_name]
        
        session = get_session()
        headers = get_headers()
        try:
            url = CourseTOCFetcher.BASE_URL.format(kurso_name)
            response = session.get(url,data={},headers=headers)
            if response.status_code == 200:
                kurso_data = response.json()
                #save it to kurso_toc map
                self.kursos_toc[kurso_name] = kurso_data
                return self.kursos_toc[kurso_name]
            else:
                return "Request failed"
    
        except Exception as e:
            print(f"Failed to get the toc for {kurso_name}.\nReason {e}")
        
                
            