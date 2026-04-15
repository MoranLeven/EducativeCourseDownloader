from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Video")
def Video(content, session, headers, pageObj):
    '''
    {
     "type": "Video",
     "mode": "edit",
     "content": {
          "version": "1.0",
          "height": "450px",
          "url": "https://www.youtube.com/watch?v=rFcbVrQWJSU",
          "comp_id": "HP6INFO03WKQnkvsut6dC"
     },
     "iteration": 0,
     "hash": 2,
     "saveVersion": 1
}
    '''
    return "<h2>I'm a simple Video Component</h2>"
