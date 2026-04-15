# The SearchQueryBuilder follows builder pattern to build a payload
import json


class SearchQueryBuilder:

    def __init__(self):
        self._query = ""
        self._page = ""
        self._page_size = ""
        self._filters = '{"collection_type":["collection"]}'
        self._range_filters = '{}'

    def query(self, q):
        self._query = q.strip()
        return self

    def page(self, page):
        self._page = str(page)
        return self

    def page_size(self, page_size):
        self._page_size = str(page_size)
        return self

    def filters(self, filters):
        self._filters = filters
        return self

    def range_filters(self, range_filters):
        self._range_filters = range_filters
        return self

    def build(self):
        payload = {
            "query": self._query,
            "page": self._page,
            "page_size": self._page_size,
            "filters": self._filters,
            "range_filters": self._range_filters,
        }
        return json.dumps(payload)
