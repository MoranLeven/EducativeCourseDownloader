from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("ButtonLink")
def ButtonLink(content, session, headers, pageObj):
    '''
    {
     "type": "ButtonLink",
     "mode": "edit",
     "content": {
          "version": "1.0",
          "content": {
               "url": "",
               "buttonText": "''",
               "openInNewTab": false,
               "loginRequired": false,
               "buttonType": "Default"
          },
          "comp_id": "q-fSIoyg71-ZPcDjG3zKg",
          "url": "https://www.educative.io/path/become-a-java-developer",
          "buttonText": "Become a Java Developer",
          "buttonType": "Primary",
          "openInNewTab": true
     },
     "iteration": 26,
     "hash": 1,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "iuC2FpV1kjKCky96wFVA5"
}
    '''
    return "<h2>I'm a simple ButtonLink Component</h2>"
