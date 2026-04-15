from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("LiveApp")
def LiveApp(content, session, headers, pageObj):
    '''
    {
     "type": "LiveApp",
     "mode": "edit",
     "content": {
          "height": "450px",
          "comp_id": "ab8cf7ce-8166-4de6-bd8b-c51099d53cbf",
          "appUrl": "/notebooks/FineTuneModelParameters.ipynb",
          "url": "",
          "imageUrl": "/udata/XDxaZxPqwoQ/Kaggle-Challenge---Fine-Tune-Parameters.jpg",
          "dockerExecutionContext": {
               "imageName": "author-4747639511842816-collection-6260527028240384-rev-8-container-4837277949755392-jupyerdocker3",
               "job": {
                    "runInLiveContainer": true,
                    "name": "jupyter_job",
                    "startScript": "echo \"hello world\"",
                    "inputFileName": "helloworld.ipnyb",
                    "key": "d9882fc5-e40c-456a-86ee-dea4d7e9242f",
                    "runScript": "nohup jupyter notebook /usr/local/notebooks/helloworld.ipynb --allow-root --no-browser > /dev/null 2>&1 &",
                    "ports": "8080"
               },
               "envs": [],
               "liveInstance": {
                    "url": "https://1d8y2d68knjl5.educative.run",
                    "id": "1d8y2d68knjl5"
               }
          },
          "version": "1.0",
          "entryFileName": "helloworld.ipnyb",
          "dockerJob": {
               "runInLiveContainer": true,
               "name": "jupyter_job",
               "startScript": "echo \"hello world\"",
               "inputFileName": "helloworld.ipnyb",
               "key": "d9882fc5-e40c-456a-86ee-dea4d7e9242f",
               "runScript": "nohup jupyter notebook /usr/local/notebooks/helloworld.ipynb --allow-root --no-browser > /dev/null 2>&1 &",
               "ports": "8080"
          }
     },
     "hash": "13",
     "iteration": 0
}
    '''
    return "<h2>I'm a simple LiveApp Component</h2>"
