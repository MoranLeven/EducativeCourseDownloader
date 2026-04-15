from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("InstaCalc")
def InstaCalc(content, session, headers, pageObj):
    '''
    {
     "type": "InstaCalc",
     "mode": "view",
     "content": {
          "version": 1,
          "title": "Spark Estimations Calculator",
          "rows": 5,
          "cols": 2,
          "showHeaders": false,
          "data": [
               [
                    {
                         "key": "A1",
                         "val": "Input file size (MB)",
                         "expr": "Input file size (MB)",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    },
                    {
                         "key": "B1",
                         "val": "25600000",
                         "expr": "25600000",
                         "hidden": false,
                         "readOnly": false,
                         "className": "",
                         "color": "#ffe599"
                    }
               ],
               [
                    {
                         "key": "A2",
                         "val": "Tasks estimation",
                         "expr": "Tasks estimation",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    },
                    {
                         "key": "B2",
                         "val": 100000,
                         "expr": "=B1/256",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    }
               ],
               [
                    {
                         "key": "A3",
                         "val": "RAM size (MB)",
                         "expr": "RAM size (MB)",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    },
                    {
                         "key": "B3",
                         "val": "25600",
                         "expr": "25600",
                         "hidden": false,
                         "readOnly": false,
                         "className": "",
                         "color": "#ffe599"
                    }
               ],
               [
                    {
                         "key": "A4",
                         "val": "Partition estimation in a filter worker",
                         "expr": "Partition estimation in a filter worker",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    },
                    {
                         "key": "B4",
                         "val": 100,
                         "expr": "=B3/256",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    }
               ],
               [
                    {
                         "key": "A5",
                         "val": "Workers estimation",
                         "expr": "Workers estimation",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    },
                    {
                         "key": "B5",
                         "val": 2020,
                         "expr": "=B2/B4+2*B2/(B4*2)+(B2/B4+2*B2/(B4*2))/100",
                         "hidden": false,
                         "readOnly": true,
                         "className": ""
                    }
               ]
          ],
          "comp_id": "sLzNi1q0t0WdaTL2Gn_h_"
     },
     "contentID": "LLVpRUt5EExKcnE9Ba20L",
     "saveVersion": 6,
     "iteration": 0,
     "hash": 8,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal"
}
    '''
    return "<h2>I'm a simple InstaCalc Component</h2>"
