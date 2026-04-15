from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("VideoRecorder")
def VideoRecorder(content, session, headers, pageObj):
    '''
    {
     "type": "VideoRecorder",
     "mode": "view",
     "content": {
          "version": "1.0",
          "content": {
               "timeLimit": 60
          },
          "comp_id": "f338b061-8734-4974-b9c2-26c5f26e3901",
          "timeLimit": "120"
     },
     "hash": "2",
     "iteration": 0
}
    '''
    return "<h2>I'm a simple VideoRecorder Component</h2>"
