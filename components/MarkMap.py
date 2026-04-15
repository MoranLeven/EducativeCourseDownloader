from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("MarkMap")
def MarkMap(content, session, headers, pageObj):
    '''
    {
     "type": "MarkMap",
     "mode": "edit",
     "content": {
          "version": "1.0",
          "caption": "The advanced design problems that will be covered in this course",
          "height": 500,
          "width": 900,
          "text": "# Advanced design problems\n- YouTube \n- Quora\n- Google maps\n- Proximity service/Yelp\n- Uber\n- Twitter\n- Newsfeed system\n- Instagram\n- URL shortening service/TinyURL\n- Web crawler\n- WhatsApp\n- Typeahead suggestion service\n- Collaborative document/Google docs\n- ChatGPT system\n",
          "comp_id": "vNk15TzLJ2TjdqRwQ4Dcn"
     },
     "iteration": 1,
     "hash": 3,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "F6NBKf3whxS9vjzZ9FaQX",
     "saveVersion": 12,
     "headingTag": "dtR7WqiJvoa4n1vrG3SV-",
     "collapsed": true
}
    '''
    return "<h2>I'm a simple MarkMap Component</h2>"
