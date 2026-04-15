import os
from .utilities import get_session, get_headers
from concurrent.futures import ThreadPoolExecutor
import re
# Import the renderer we created above
from .pagerenderer import PageRenderer 
from .extras import CSS_STYLE, JS_SCRIPT
import json


class CourseChapterFetcher:
    BASE_URL = "https://www.educative.io/api/collection/{}/{}/page/{}?work_type=collection"

    def __init__(self):
        self.courseTOC = ""
        self.outputDIR = ""
        self.toc = {}
        self.cssDIR = ""
        self.jsDIR = ""
        self.indexDIR = ""
        # Initialize the Renderer
        # We pass the session so the renderer can reuse cookies for images
        self.renderer = PageRenderer()

    def extractTOC(self):
        print("⏳ Extracting TOC details...")
        self.categories = self.courseTOC.get("instance", {}).get("details", {}).get("toc", {}).get("categories", [])
        self.author_id = self.courseTOC.get('instance',{}).get('details',{}).get('author_id')
        self.collection_id = self.courseTOC.get('instance',{}).get('details',{}).get('collection_id')
        self.outputDIR = self.sanitize_filename(self.courseTOC.get('instance',{}).get('details',{}).get('title'))
        self.jsDIR = os.path.join(self.outputDIR,"script.js")
        self.cssDIR = os.path.join(self.outputDIR,"style.css")
        self.indexDIR = os.path.join(self.outputDIR,"index.html")
        self.assetsDIR = os.path.join(self.outputDIR,"assets")
        
        self.toc = {}
        
    def sanitize_filename(self, name):
        return re.sub(r'[<>:"/\\|?*\n\r]', '', name).replace(" ", "_")
        
    def downloadCourse(self,courseTOC):
        self.courseTOC = courseTOC
        self.extractTOC()
        print("⬇️ Course downloading started ...")
        # Create base directory
        if not os.path.exists(self.outputDIR):
            os.makedirs(self.outputDIR)
        
        # Create assets directory
        if not os.path.exists(self.assetsDIR):
            os.makedirs(self.assetsDIR)

        #download all the chapters along with the pages
        for ch_idx, chapter in enumerate(self.categories):
            chapterTitle = f"{ch_idx+1:02d}_{self.sanitize_filename(chapter.get('title'))}"
            
            print(f"\n📂 Processing Chapter {ch_idx+1}: {chapterTitle}")

            # Create Directory for this Chapter
            chapter_path = os.path.join(self.outputDIR, chapterTitle)
            if not os.path.exists(chapter_path):
                os.makedirs(chapter_path)
                
            pages = chapter.get('pages', [])
            tasks = [page.get('id') for page in pages]
            ordered_page_data = self.getPages(tasks)
            # Convert and Save
            self.downloadChapter(ordered_page_data,tasks,chapterTitle)
        
        # create the style.css, script.js and index.html file
        
        with open(self.cssDIR,'w',encoding='utf-8') as css:
            css.write(CSS_STYLE)
            print("Added stylesheet file")
            
        with open(self.jsDIR,'w',encoding='utf-8') as js:
            js.write(JS_SCRIPT)
            print("Added script file")
            
        tableOfContents = self.createTOC()
        with open(self.indexDIR,'w',encoding='utf-8') as indexFile:
            indexFile.write(tableOfContents)
            print("Added Table Of Contents file")
        
        print(f"✅{self.outputDIR.replace("_"," ")} course downloaded successfully.")
    
    
    #need to work on this as well
    def downloadOfflineCourse(self,folderName,courseTOC):
        # folderName = os.path.join("KursoDownloaderLowLevelDesign",folderName)
        if not os.path.exists(folderName):
            print(f"{folderName} does not exists")
        chapters = sorted([chap for chap in os.listdir(folderName) if os.path.isdir(os.path.join(folderName,chap))])
        
        self.courseTOC = courseTOC
        self.extractTOC()
        print("⬇️ Course downloading started ...")
        
        # Create base directory
        if not os.path.exists(self.outputDIR):
            os.makedirs(self.outputDIR)
        #create the assets directory inside the basedirectory for image and other important data
        if not os.path.exists(self.assetsDIR):
            os.makedirs(self.assetsDIR)
        
        #download all the chapters along with the pages
        for ch_idx, (chapter,category) in enumerate(zip(chapters,self.categories)):
            chapter_path = os.path.join(folderName,chapter)
            output_path = os.path.join(self.outputDIR,chapter)
            files = sorted([f for f in os.listdir(chapter_path) if f.endswith('.json')])
            
            ordered_page_data = []
            pages = category.get('pages')
            tasks = [page.get('id') for page in pages]
            for file in files:
                filePath = os.path.join(chapter_path,file)
                with open(filePath,'r',encoding='utf-8') as f:
                    raw_file = json.load(f)
                    ordered_page_data.append(raw_file)
                    
            print(f"\n📂 Processing Chapter {ch_idx+1}: {chapter_path}")

     
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            # Convert and Save
            self.downloadChapter(ordered_page_data,tasks,chapter)
        
        # create the style.css, script.js and index.html file
        
        with open(self.cssDIR,'w',encoding="utf-8") as css:
            css.write(CSS_STYLE)
            print("Added stylesheet file")
            
        with open(self.jsDIR,'w', encoding='utf-8') as js:
            js.write(JS_SCRIPT)
            print("Added script file")
            
        tableOfContents = self.createTOC()
        with open(self.indexDIR,'w',encoding='utf-8') as indexFile:
            indexFile.write(tableOfContents)
            print("Added Table Of Contents file")
        
        print(f"✅{self.outputDIR.replace("_"," ")} course downloaded successfully.")
            
            

    #creates index.html 
    def createTOC(self):
        idx_html = f'<!DOCTYPE html><html><head><title>Index</title><link rel="stylesheet" href="style.css"><script src="script.js"></script></head><body><div class="container"><h1>Course Index</h1>'
        for chapTitle, lessons in self.toc.items():
            idx_html += f'<div class="widget"><div class="widget-header">{chapTitle}</div><div class="widget-body"><ul>'
            for pageName, path in lessons: idx_html += f'<li><a href="{path}">{pageName}</a></li>'
            idx_html += '</ul></div></div>'
        idx_html += '</div></body></html>'
        return idx_html

    #the downloading of the chapter pages will be multithreaded along with the page creation to speed up the downloading
    def downloadChapter(self,chapterData,pageIds,chapterTitleRank):
        totalPages = len(chapterData)
        for i, pageData in enumerate(chapterData):
                if not pageData: continue # Skip failed downloads
                
                title = pageData.get('summary', {}).get('title',chapterTitleRank[3:])
                fileName = f"{i+1:02d}_{self.sanitize_filename(title)}.html"
                filePath = os.path.join(self.outputDIR, chapterTitleRank, fileName)
                
                #add the currentChapter page to the toc dict
                self.toc.setdefault(chapterTitleRank[3:],[]).append((title,chapterTitleRank+'/'+fileName))
                #check if file path already exists if yes then ignore
                if os.path.isfile(filePath):
                    print("⏩ File already present skipping it")
                    continue
                if i < len(pageIds):
                    pageId = pageIds[i]
                else:
                    pageId = 0
                prevChapter = "" if i==0 else f"{i:02d}_{self.sanitize_filename(chapterData[i-1].get('summary',{}).get('title',chapterTitleRank[3:]))}.html"
                nextChapter = "" if i+1 == totalPages else f"{i+2:02d}_{self.sanitize_filename(chapterData[i+1].get('summary',{}).get('title',chapterTitleRank[3:]))}.html"
                # 1. Convert JSON to HTML using the Registry Renderer
                self.renderer.updatePageData(self,pageData,prevChapter,nextChapter,pageId,title, os.path.join(self.outputDIR,chapterTitleRank))
                pageHTMLContent = self.renderer.renderPageToHTML()
                # # 2. Save to File
                with open(filePath, "w", encoding="utf-8") as f:
                    f.write(pageHTMLContent)
                
                print(f"💾 Saved: {fileName}")

    def getPages(self, tasks):
        """
        Fetches pages in parallel but returns them in the exact order of 'tasks'.
        """
        max_workers = min(max(len(tasks), 1), 10)
        results = [None] * len(tasks)

        # with ThreadPoolExecutor(max_workers=max_workers) as executor:
        #     # Executor.map preserves the order of the input iterable
        #     # It blocks until results are available in order
        #     results_generator = executor.map(self.getPage, tasks)
            
        #     # Convert generator to list
        #     results = list(results_generator)

        # return results
        
        # a better approach 
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futureMap = {executor.submit(self.getPage, task):idx for idx,task in enumerate(tasks)}
            
            for future in futureMap:
                idx = futureMap[future]
                page_id = tasks[idx]
                try: 
                    results[idx] = future.result()
                except Exception as e:
                    print(f" Error while fetching the {page_id}: {e}")
        return results

    def getPage(self, page_id):
        url = self.BASE_URL.format(self.author_id, self.collection_id, page_id)
        try:
            session = get_session()
            headers = get_headers()
            response = session.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                # Inject IDs into summary for the renderer to use later
                if 'summary' not in data: data['summary'] = {}
                data['summary']['author_id'] = self.author_id
                data['summary']['collection_id'] = self.collection_id
                return data
            else:
                print(f"❌ Failed ({response.status_code}): {url}")
                return None
        except Exception as e:
            print(f"❌ Error fetching page {page_id}: {e}")
            return None