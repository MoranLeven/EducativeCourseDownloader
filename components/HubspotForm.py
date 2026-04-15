from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("HubspotForm")
def HubspotForm(content, session, headers, pageObj):
    '''
    {
     "type": "HubspotForm",
     "mode": "view",
     "content": {
          "formCta": "",
          "formDescription": "Fill out the form to download your FREE template",
          "formId": "ec38f3e4-2ba4-4f9f-a668-a54d8e46ed2e",
          "formSvg": "",
          "formTitle": "",
          "portalId": "4740448",
          "showModal": false,
          "backgroundColor": "#fafafa",
          "formBackgroundColor": "#ffffff",
          "showImage": true,
          "imageRedirectionUrl": "",
          "coverImage": {
               "file": null,
               "path": "/api/page/5179230060675072/image/download/5321465899909120",
               "metadata": {
                    "width": 2133,
                    "height": 1500,
                    "sizeInBytes": 64429,
                    "name": "system design template download button.png"
               }
          },
          "comp_id": "sBqF4s7QtQZM-O5hM-CgZ",
          "isCopied": true
     },
     "status": "normal",
     "contentID": "WYkPFB5zICR3xNGj4NPOt",
     "saveVersion": 14,
     "widgetCopyId": null,
     "iteration": 0,
     "hash": 1,
     "children": [
          {
               "text": ""
          }
     ]
}
    '''
    return "<h2>I'm a simple HubspotForm Component</h2>"
