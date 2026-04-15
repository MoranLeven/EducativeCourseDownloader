from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Adaptive")
def Adaptive(content, session, headers, pageObj):
    '''
    {
     "type": "Adaptive",
     "mode": "edit",
     "content": {
          "tabs": {
               "defaultTab": {
                    "id": "defaultTab",
                    "parentId": "",
                    "name": "",
                    "comps": []
               },
               "JvbK77N_4DsLMvXzks110": {
                    "id": "JvbK77N_4DsLMvXzks110",
                    "name": "Sending media files",
                    "comps": [
                         {
                              "type": "SlateHTML",
                              "content": {
                                   "html": "<p id=\"2wUR77x78pzMiJUpmPPMS\">When a user sends a media file, the chat app encrypts it locally using end-to-end encryption (E2EE) before upload. This ensures the file remains unreadable during transmission. The encrypted file is uploaded to a file service, which stores it temporarily in encrypted blob storage (e.g., AWS S3 or GCS), as shown below:</p>",
                                   "comp_id": "2wUR77x78pzMiJUpmPPMS"
                              },
                              "hash": 0
                         },
                         {
                              "type": "DrawIOWidget",
                              "mode": "edit",
                              "content": {
                                   "path": "/api/collection/10370001/6717151969673216/page/4582468133715968/image/6739135722029056?page_type=collection_lesson",
                                   "caption": "The flow to store and send a media file in the chat application",
                                   "editorImagePath": "/api/collection/10370001/6717151969673216/page/4582468133715968/image/5330236661956608?page_type=collection_lesson",
                                   "version": 2,
                                   "height": 331,
                                   "width": 534,
                                   "editorGCSImagePath": "educative-us-central1/uc/v5/10370001/collections/6717151969673216/rev-2/pages/4582468133715968/images/5330236661956608-2025-05-23T06:22:04.322664",
                                   "slidesEnabled": true,
                                   "isSlides": false,
                                   "slidesCaption": [],
                                   "redirectionUrl": "",
                                   "borderColor": "#ffffff",
                                   "comp_id": "kZBHR2T8sHS66YwJYDl7J",
                                   "slidesId": ""
                              },
                              "iteration": 3,
                              "hash": 1,
                              "children": [
                                   {
                                        "text": ""
                                   }
                              ],
                              "status": "normal",
                              "contentID": "2GiszzSfBGKfoWGGH7Zpn",
                              "widgetCopyId": "6717151969673216"
                         },
                         {
                              "type": "SlateHTML",
                              "content": {
                                   "html": "<p id=\"j7-iHEnQ5mZjYPgXIcc5o\">Instead of sending the file directly, the file service returns a signed URL<strong>, </strong>a short-lived link that grants access to the encrypted file. This URL is sent to the recipient via WebSockets.</p><p id=\"646vIHjr8i-kT4zI-Geqk\">The recipient then downloads and decrypts the file locally, ensuring that it can be viewed on the app. Once decrypted, the file is saved locally for offline access. </p><blockquote id=\"IqKEiven4xt5NHrNaAJf1\"><p><strong>Note:</strong> The media file is never permanently stored on the backend and is deleted once the recipient acknowledges after a specified time, let\u2019s say 30 days.</p></blockquote><p id=\"22L3sOm5A7r9xI9E9A--F\"></p>",
                                   "comp_id": "j7-iHEnQ5mZjYPgXIcc5o"
                              },
                              "hash": 2
                         }
                    ],
                    "parentId": "defaultTab"
               },
               "FWLZSgV7zXtfjJhq8hXqr": {
                    "id": "FWLZSgV7zXtfjJhq8hXqr",
                    "name": "Offline messages",
                    "comps": [
                         {
                              "type": "SlateHTML",
                              "content": {
                                   "html": "<p id=\"dYlpOWTsp55QZZLt4GzyW\">We know from the previous lesson that undelivered messages are kept temporarily in a queue when the recipient is offline. Later, when users are online, a push notification notifies the recipient about the new message, and the WebSocket connection is established. In the next step, the messages are delivered via the WebSocket connection in the format shown below:</p>",
                                   "comp_id": "dYlpOWTsp55QZZLt4GzyW"
                              },
                              "hash": 0
                         },
                         {
                              "type": "Code",
                              "mode": "edit",
                              "content": {
                                   "version": "8.0",
                                   "caption": "The response that contains the offline messages to be delivered when a user comes online",
                                   "language": "yaml",
                                   "title": "",
                                   "theme": "default",
                                   "additionalContent": [],
                                   "selectedIndex": 0,
                                   "runnable": false,
                                   "judge": false,
                                   "staticEntryFileName": true,
                                   "judgeContent": "",
                                   "judgeHints": "",
                                   "allowDownload": false,
                                   "treatOutputAsHTML": false,
                                   "enableHiddenCode": false,
                                   "enableStdin": false,
                                   "evaluateWithoutExecution": false,
                                   "showSolution": false,
                                   "timeLimit": 30,
                                   "hiddenCodeContent": {
                                        "prependCode": "\n\n",
                                        "appendCode": "\n\n",
                                        "codeSelection": "prependCode"
                                   },
                                   "dockerJob": {},
                                   "selectedApiKeys": {},
                                   "selectedEnvVars": {},
                                   "specialInput": "no-input",
                                   "solutionContent": "\n\n\n",
                                   "judgeContentPrepend": "\n\n\n",
                                   "evaluateLanguage": "yaml",
                                   "isCodeDrawing": false,
                                   "content": "{\n\"messages\": [\n     { \n       \"payload\": [\n           {  //message-01\n              \"senderId\"       : \"Rtnukkald=\",        \n              \"receiverId\"     : \"IJUkalxUl=\",                   \n              \"messageId\"      : \"Pqwnkilsx=\",         \n              \"timestamp\"      : \"9:47:30PM 12-1-2025\",       \n              \"attachment\"     : true,     \n              \"attachmentURI\"  : \"/v1.0/asset/{id}\",    \n              \"messageText\"    : \"Hello, Welcome to Educative!\"         \n          },\n         {   //message-02\n             \"senderId\"       : \"alnukRtkald=\",        \n             \"receiverId\"     : \"IJUkalxUl=\",                   \n             \"messageId\"      : \"Xkilqwnsx=\",         \n             \"timestamp\"      : \"9:47:50PM 12-1-2025\",       \n             \"attachment\"     : true,     \n             \"attachmentURI\"  : \"/v1.0/asset/{id}\",    \n             \"messageText\"    : \"Hi!\"         \n        },\n       ...\n       //and so on.\n    ]}\n  }",
                                   "comp_id": "ZTA9kj7xm2jKQ3gMAgPCA",
                                   "entryFileName": "index.yaml",
                                   "staticEntryName": false,
                                   "defaultSelectedFile": "index.yaml"
                              },
                              "iteration": 2,
                              "hash": 1,
                              "children": [
                                   {
                                        "text": ""
                                   }
                              ],
                              "status": "normal",
                              "contentID": "_eV1hNsI03c9I8Vf0Khhw",
                              "saveVersion": 5,
                              "widgetCopyId": "6717151969673216"
                         }
                    ],
                    "parentId": "defaultTab"
               }
          },
          "children": {
               "defaultTab": [
                    "JvbK77N_4DsLMvXzks110",
                    "FWLZSgV7zXtfjJhq8hXqr"
               ],
               "JvbK77N_4DsLMvXzks110": [],
               "FWLZSgV7zXtfjJhq8hXqr": []
          },
          "version": 2,
          "comp_id": "HjFnOCXYcKoCFfCgbMsW8"
     },
     "iteration": 0,
     "hash": 20,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "XGtNiKdVKy6AzbDUf2rH4",
     "headingTag": "-j7crxwDNvAkb3pSkLVGO",
     "collapsed": true
}
    '''
    return "<h2>I'm a simple Adaptive Component</h2>"
