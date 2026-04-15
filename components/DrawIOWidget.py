from ..componentregistry import ComponentRegistry
from .computilities import (
    fetchSlideImageIds,
    saveImage,
    getSVG,
    renderSimpleCarousel,
)
import re


@ComponentRegistry.register("DrawIOWidget")
def DrawIOWidget(content, session, headers, pageObj):
    html = "Failed to get DrawIOWidget"
    if content.get("isSlides"):
        # Simple Image Slides
        slides_id = content.get("slidesId")
        imgPathTemplate = content.get("editorImagePath", "")
        captionList = content.get("slidesCaption", [])
        if slides_id:
            ids = fetchSlideImageIds(slides_id)
            html = renderSimpleCarousel(ids,captionList,pageObj)
    else:
        path = content.get("path") or content.get("editorImagePath")
        caption = content.get('caption')
        imageId = path.split("?")[0].split("/")[-1]
        svg = getSVG(imageId, pageObj)
        html = f"<span title='{caption}'>{svg}</span>"
       
    return html
