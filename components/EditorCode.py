from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("EditorCode")
def EditorCode(content, session, headers, pageObj):
    '''
    {
     "type": "EditorCode",
     "mode": "edit",
     "content": {
          "version": "1.0",
          "comp_id": "X9XkVqndj1a7JYagN_aFc",
          "language": "plainText",
          "content": "{\n    build_version: build:1.1\n}"
     },
     "iteration": 0,
     "hash": 24,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "_bivrk-aq-Yf_08RijmOz",
     "saveVersion": 5,
     "headingTag": "xYti2e6eBO5QyQwFxwe1n",
     "collapsed": true,
     "widgetCopyId": "6521687034822656"
}
    '''
    return "<h2>I'm a simple EditorCode Component</h2>"
