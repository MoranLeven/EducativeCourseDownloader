from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("VNC")
def VNC(content, session, headers, pageObj):
    '''
    {
     "type": "VNC",
     "mode": "edit",
     "content": {
          "version": 4,
          "theme": "default",
          "showLineNumbers": true,
          "showConsole": false,
          "hideCodeView": false,
          "hideResultOutput": false,
          "hideOutputUrl": false,
          "loaders": {
               "java": {
                    "title": "Java - Swing",
                    "dockerJob": {
                         "runScript": "export DISPLAY=:1.0 && echo \"Cleaning directory...\" && cd /usercode && rm -f *.class && (pkill java || true) && echo \"Compiling...\" && javac Main.java && echo \"Executing Program...\" && java -Dsun.java2d.xrender=false Main",
                         "entryFile": "Main.java"
                    },
                    "enabled": true,
                    "dockerImage": "gui-app-hello-world"
               },
               "pythonTk": {
                    "title": "Python - tkinter",
                    "dockerJob": {
                         "runScript": "cd /usercode && export DISPLAY=:1.0 && echo \"Executing Program...\" && python3.8 main.py",
                         "entryFile": "main.py"
                    },
                    "enabled": false,
                    "dockerImage": "gui-app-hello-world"
               }
          },
          "npmPackages": {},
          "outputHeight": 600,
          "dockerJob": {
               "key": "3xPQy_GnT1t54tQ_BJ60f",
               "name": "Azure Chrome Job",
               "inputFileName": "foo",
               "runScript": "export DISPLAY=:1.0; useradd -m chromeuser; google-chrome https://dev.azure.com --no-sandbox",
               "jobType": "GUI",
               "forceRelaunchOnCompChange": true,
               "runInLiveContainer": true,
               "ports": 8080,
               "startScript": ""
          },
          "codeContents": {
               "module": "/",
               "id": 0,
               "maxId": 4,
               "selectedId": 4,
               "children": [
                    {
                         "id": 4,
                         "module": "pipeline.yaml",
                         "leaf": true,
                         "parentId": 0,
                         "data": {
                              "content": "trigger:\n  branches:\n    include:\n    - master\nstages:\n- stage: __default\n  jobs:\n  - job: Job\n    pool:\n      vmImage: ubuntu-latest\n    steps:\n    - task: Bash@3\n      displayName: Create Java Test Image\n      inputs:\n        targetType: inline\n        script: docker build -t seleniumtests .\n    - task: Bash@3\n      displayName: Run Java Test Container\n      inputs:\n        targetType: inline\n        script: docker run -e \"BROWSER=chrome\" --name tests seleniumtests\n    - task: Bash@3\n      displayName: Start Java Test Container\n      condition: always()\n      inputs:\n        targetType: inline\n        script: docker start tests\n    - task: Bash@3\n      displayName: Copy Screenshots From Run Java Test Container\n      condition: always()\n      inputs:\n        targetType: inline\n        script: docker cp tests:/target/screenshots screenshots\n    - task: Bash@3\n      displayName: Copy Logs From Run Java Test Container\n      condition: always()\n      inputs:\n        targetType: inline\n        script: docker cp tests:/target/logs logs\n    - task: Bash@3\n      displayName: Copy Test-Output From Run Java Test Container\n      condition: always()\n      inputs:\n        targetType: inline\n        script: docker cp tests:/target/surefire-reports testoutput\n    - task: Bash@3\n      displayName: Display Folders from Default Working Directory\n      condition: always()\n      inputs:\n        targetType: inline\n        script: ls $(System.DefaultWorkingDirectory)\n    - task: PublishPipelineArtifact@1\n      condition: always()\n      inputs:\n        targetPath: $(System.DefaultWorkingDirectory)/screenshots\n        publishLocation: pipeline\n        artifact: screenshots\n    - task: PublishPipelineArtifact@1\n      condition: always()\n      inputs:\n        targetPath: $(System.DefaultWorkingDirectory)/logs\n        publishLocation: pipeline\n        artifact: logs\n    - task: PublishTestResults@2\n      condition: always()\n      inputs:\n        testResultsFormat: JUnit\n        testResultsFiles: '**/junitreports/TEST-*.xml'",
                              "language": "javascript",
                              "staticFile": false,
                              "hidden": false,
                              "highlightedLines": "64 68"
                         },
                         "hideFile": false,
                         "enableHiddenCode": false
                    }
               ],
               "judge": {
                    "judgeActive": false
               },
               "hideFile": true,
               "enableHiddenCode": true
          },
          "caption": "Chrome Live Container",
          "comp_id": "XRWSulJMGRidRyQRt3kpR"
     },
     "iteration": 0,
     "hash": 3,
     "saveVersion": 2
}
    '''
    return "<h2>I'm a simple VNC Component</h2>"
