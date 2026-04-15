from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("File")
def File(content, session, headers, pageObj):
    '''
    {
     "type": "File",
     "mode": "edit",
     "content": {
          "image_id": 4933663715229696,
          "file_name": "SeleniumJava.zip",
          "text": "",
          "file": null,
          "metadata": {
               "sizeInBytes": 73053
          },
          "comp_id": "Yml3pkRfo1-7woOpBJ2SX"
     },
     "iteration": 0,
     "hash": 2,
     "saveVersion": 7
}
    '''
    return "<h2>I'm a simple File Component</h2>"
