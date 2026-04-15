# search the courses and return a list
import json
from .utilities import get_session, get_headers
from .SearchQueryBuilder import SearchQueryBuilder

class CourseSearch:
    URL = "https://www.educative.io/api/search/collection-search"
    
    def __init__(self)->None:
        self.urls_slugs = {}
        self.session = get_session()
    
    def busco(self,q=""):
        q = q.strip()
        #if q already in self.urls_slugs return from there
        if q in self.urls_slugs:
            return self.urls_slugs[q]
        
        if q == "":
            return "[🔎] Try to search something better!!"
        
        sq = SearchQueryBuilder()
        payload = (sq
                   .query(q)
                   .page(0)
                   .page_size(20)
                   .build())
                   
        headers = get_headers()
        
        try:
            response = self.session.post(self.URL,data=payload,headers=headers)
            if response.status_code == 200:
                queryData = response.json()
                if queryData:
                    self.urls_slugs[q] = self.__get_urls_slugs(queryData)
                    # print(self.urls_slugs[q],end="\n\n")
                else:
                    print("Oppss.. No result found.")
            else:
                return response
        except Exception as e:
            print(f"❌ Failed to search for {q}.")
            return []
    
    def __get_urls_slugs(self,queryData):
        urls_slugs = []
        if queryData:
            searchResults = queryData.get("hits",{}).get("hits",[])
            for result in searchResults:
                url_slug = result.get('_source',{}).get('url_slug',"")
                if url_slug:
                    urls_slugs.append(url_slug)
        return urls_slugs
            

    def get(self,query):
        if query.strip() in self.urls_slugs:
            return self.urls_slugs[query.strip()]
        else:
            return []
        

