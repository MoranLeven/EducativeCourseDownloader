import re
from ..utilities import get_headers, get_session
import os
import uuid

BASE_URL = "https://www.educative.io"



def clean_html(html_text):
    if not html_text: return ""
    html_text = re.sub(r'<keyword><word>(.*?)</word><meaning>(.*?)</meaning></keyword>', r'<strong>\1</strong>', html_text)
    html_text = re.sub(r'<callout.*?>', r'<div style="background:#e3f2fd;padding:10px;margin:10px 0;">', html_text)
    html_text = html_text.replace('</callout>', '</div>')
    return html_text

# def fetch_lazy_component(author_id, collection_id, page_id, revision, index):
#     url = f"{BASE_URL}/api/collection/{author_id}/{collection_id}/page/{page_id}/{revision}/{index}?work_type=collection"
#     try:
#         res = SESSION.get(url, headers=HEADERS)
#         if res.status_code == 200: return res.json()
#     except Exception as e: print(f"Error fetching lazy component: {e}")
#     return None

def saveImage(imageId,pageObj,extension):
    
    authorId = pageObj.authorId
    collectionId = pageObj.collectionId
    pageId = pageObj.pageId
    url = f"{BASE_URL}/api/collection/{authorId}/{collectionId}/page/{pageId}/image/{imageId}"
    
    session = get_session()
    headers = get_headers()
    
    try:
        response = session.get(url,headers=headers,timeout=20)
        fileName = f"{pageId}.{extension}"
        filePath = os.path.join(pageObj.assetsDIR,fileName)
        if response.status_code == 200:
            with open(filePath,'wb') as ifile:
                ifile.write(response.content)
        
        return f"../assets/{fileName}"
            
    except Exception as e:
        print(f"❌ Failed to fetch image_Id {imageId} : \n{e}",end='\r')
        return "../assets/fail.png"
    
    #this method will return the location where the image is downloaded

def getSVG(imageId,pageObj):
    authorId = pageObj.authorId
    collectionId = pageObj.collectionId
    pageId = pageObj.pageId
    url = f"{BASE_URL}/api/collection/{authorId}/{collectionId}/page/{pageId}/image/{imageId}"
    
    session = get_session()
    headers = get_headers()
    
    try:
        response = session.get(url,headers=headers,timeout=20)
        if response.status_code == 200:
            #check if the content_type contains svg
            svg = response.content 
            return svg.decode(encoding='utf-8')
    except Exception as e:
        print(f"❌ Failed to fetch image_Id {imageId} : \n{e}",end='\r')
        return "<svg><p>Failed to download svg</p></svg>"


def fetchSlideImageIds(slides_id):
    url = f"{BASE_URL}/api/slides/data?slides_id={slides_id}"
    try:
        session = get_session()
        headers = get_headers()
        res = session.get(url, headers=headers)
        if res.status_code == 200:
            return res.json().get("image_ids", [])
    except Exception as e: 
        print(f"❌ Failed to fetch the images slides due to : {e}")
    return []

def renderSimpleCarousel(imageIds,captionList,pageObj):
    if not imageIds and captionList: return ""
    carousel_id = f"slide_{uuid.uuid4().hex[:8]}"
    count = len(imageIds)
    html = f'''<div class="slideshow-container" id="{carousel_id}"><div class="numbertext">1 / {count}</div><a class="prev" onclick="moveSlide('{carousel_id}', -1)">&#10094;</a><a class="next" onclick="moveSlide('{carousel_id}', 1)">&#10095;</a>'''
    for i, (imgId,caption) in enumerate(zip(imageIds,captionList)):
        svg = getSVG(imgId,pageObj)
        ac = "active" if i==0 else ""
        if svg: html += f'<div class="mySlides {ac}"><span title="{caption}">{svg}</span></div>'
    html += f'</div><script>initSlide("{carousel_id}", {count});</script>'
    return html