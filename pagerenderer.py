from concurrent.futures import ThreadPoolExecutor, as_completed
from .utilities import get_session, get_headers, trace
from .extras import CSS_STYLE
import os
from .componentregistry import ComponentRegistry
# from . import components

class PageRenderer:

    def __init__(self):
        self.pageData = ""
        self.next = ""
        self.prev = ""
        self.authorId = ""
        self.html = ""
        self.collectionId = ""

    def updatePageData(self, courseObj, pageData, prev, next, pageId, pageTitle, chapterPath ):
        self.pageData = pageData
        self.prev = prev
        self.next = next
        self.pageTitle = pageTitle
        self.chapterPath = chapterPath
        self.pageId = pageId
        self.pageObj = courseObj
        self.authorId = courseObj.author_id
        self.collectionId = courseObj.collection_id
        self.indexDIR = courseObj.indexDIR
        self.styleDIR = courseObj.cssDIR
        self.scriptDIR = courseObj.jsDIR
        self.assetsDIR = courseObj.assetsDIR
        self.html = ""
        self.head = ""
        self.summary = ""
        self.renderedComponents = ""
        self.footer = ""

    def renderPageToHTML(self):
        # this method will update the render all the components of pagedata to html page
        components = self.pageData.get("components")
        summary = self.pageData.get("summary")

        # 1: loop through all components of the pageData
        renderedCompData = self.getComponents(components)

        # 2: update the head
        self._addHead()
        # 3: get the component data and append it to body
        self._addBody(summary, renderedCompData)
        # 4: update the prev and next
        self._addPrevNextChapter()
        # 5: return the rendered html page
        self._constructHTMLPage()

        return self.html

    # get component uses multithreading to render the page components
    def getComponents(self, compTasks):
        max_workers = min(max(len(compTasks), 1), 10)
        results = [None]*len(compTasks)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futureIndex = {executor.submit(self.getComponent,compTask):idx for idx,compTask in enumerate(compTasks)}
            
            for future in as_completed(futureIndex):
                idx = futureIndex[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    print(f"❌ Failed to render the components : {e}")
                    results[idx] = ""
        

        return results

    @trace
    def getComponent(self, compData):
        
        type = compData.get("type")
        content = compData.get("content", {})

        handler = ComponentRegistry.get_handler(type)
        if handler:
            session = get_session()
            headers = get_headers()
            data =  handler(content, session, headers, self)
            return data
        else:
            return ""

    def _addHead(self):

        self.head = f"""
                <link rel="stylesheet" href="../style.css">
                <title>{self.pageTitle}</title>
                <script src="../script.js"></script>
        """

    def _addBody(self, summary, renderedData):
        # update the title and description of the page
        self._addTitleAndDescription(summary)
        for rData in renderedData:
            if rData:
                self.renderedComponents += rData

    def _addPrevNextChapter(self):

        self.footer = f"""
        <div class="nav-links">
            {'<a href="../index.html">📄Index</a>' if (not self.prev) else '<a href='+self.prev+' class="nav-btn">&larr;Previous</a>'}
            
            {'<a href="../index.html">📄Index</a>' if (not self.next and self.prev) else '<a href='+self.next+' class="nav-btn"">Next&rarr;</a>'}   
            
        </div>        
        """

    def _addTitleAndDescription(self, summary):
        # this method will add index page link
        # title and description of the page
        title = summary.get("title", self.pageTitle)
        description = summary.get(
            "description", "No description available for this page"
        )
        indexPagePath = self.indexDIR

        self.summary = f"""
            <div class="chapterSummary">
                <div class="indexLink"><a href="../index.html">📄Index</a></div>
                <div class='title'><h2>{title}</h2></div>
                <div class='description'><h4>{description}</h4></div>
            </div>
        """

    def _constructHTMLPage(self):
        self.html = f"""
            <html>
                <head>{self.head}</head>
                <body>
                {self.summary}
                {self.renderedComponents}
                {self.footer}
                </body>
            </html>
        """
