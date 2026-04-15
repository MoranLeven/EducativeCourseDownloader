from ..componentregistry import ComponentRegistry
from .computilities import saveImage, getSVG

@ComponentRegistry.register("Image")
def Image(content, session, headers, pageObj):
     
     '''
     {
     "type": "Image",
     "mode": "view",
     "content": {
          "image_id": 5687280266117120,
          "style": "original",
          "caption": "",
          "file": null,
          "metadata": {
               "width": 774,
               "height": 181,
               "sizeInBytes": 26442
          },
          "comp_id": "a979b7bd-d771-47a2-a6ba-38c8a93fa611"
     },
     "hash": "10",
     "iteration": 0
     }
     '''
     imageId = content.get('image_id',"") or content.get('editorImagePath')
     caption = content.get('caption',"") or "No caption available"
     metadata = content.get("metadata")
     name = metadata.get('name')
     fileType = name.split(".")[-1]
     html = ""
     if fileType.lower() == "svg":
          html += getSVG(imageId,pageObj)
     else:
          width = metadata.get('width',720)
          height = metadata.get('height',360)
          imgPath = saveImage(imageId,pageObj,fileType)
          html = f"<img src='{imgPath}' title='{caption}' width='{width}px' height='{height}px' >"
     return html