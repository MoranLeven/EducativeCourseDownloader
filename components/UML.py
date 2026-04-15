from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("UML")
def UML(content, session, headers, pageObj):
    '''
    {
     "type": "UML",
     "mode": "edit",
     "content": {
          "version": "7.0",
          "uml_widget_version": 1,
          "caption": "",
          "language": "plantuml",
          "title": "",
          "imageId": "",
          "theme": "default",
          "additionalContent": [],
          "selectedIndex": 0,
          "runnable": true,
          "judge": false,
          "staticEntryFileName": true,
          "judgeContent": null,
          "judgeHints": null,
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
          "solutionContent": "\n\n",
          "judgeContentPrepend": "\n\n\n",
          "evaluateLanguage": "plantuml",
          "isCodeDrawing": true,
          "centerOutput": true,
          "fullWidthFileOutput": true,
          "entryFileName": "diagram.java",
          "content": "@startuml\nscale 400 width\n\n\nclass Student {\n  Name\n}\nStudent \"0..*\" - \"1..*\" Course\n(Student, Course) .. Enrollment\n\nclass Enrollment {\n  drop()\n  cancel()\n}\n\ncaption Class diagram\n@enduml\n\n'See more examples on www.plantuml.com",
          "comp_id": "ClEuALiYAFNrSk1epjV7t"
     },
     "iteration": 0,
     "hash": 4,
     "saveVersion": 2
}
    '''
    return "<h2>I'm a simple UML Component</h2>"
