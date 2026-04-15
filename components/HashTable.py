from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("HashTable")
def HashTable(content, session, headers, pageObj):
    '''
    {
     "type": "HashTable",
     "mode": "edit",
     "content": {
          "version": "3.0",
          "caption": "",
          "svg_string": "<svg width=\"331pt\" height=\"109pt\" viewBox=\"0.00 0.00 330.98 109.00\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"> <g id=\"graph0\" class=\"graph\" transform=\"scale(1 1) rotate(0) translate(4 105)\"> <title>%19</title> <!-- node_2 --> <g id=\"node_2\" class=\"node\"><title>node_2</title> <polygon fill=\"#bfefff\" stroke=\"#000000\" stroke-width=\"0.42\" points=\"0,-0.5 0,-30.5 123,-30.5 123,-0.5 0,-0.5\"></polygon> <text text-anchor=\"middle\" x=\"61.5\" y=\"-11.1\" font-family=\"Courier,monospace\" font-size=\"16.00\">Key 3</text> </g> <!-- node_1 --> <g id=\"node_1\" class=\"node\"><title>node_1</title> <polygon fill=\"#bfefff\" stroke=\"#000000\" stroke-width=\"0.42\" points=\"0,-35.5 0,-65.5 123,-65.5 123,-35.5 0,-35.5\"></polygon> <text text-anchor=\"middle\" x=\"61.5\" y=\"-46.1\" font-family=\"Courier,monospace\" font-size=\"16.00\">Key 2</text> </g> <!-- node_1_1 --> <g id=\"node_1_1\" class=\"node\"><title>node_1_1</title> <path fill=\"#e6e6e6\" stroke=\"black\" stroke-width=\"0.5\" d=\"M168.067,-36.9C168.067,-36.9 213.925,-36.9 213.925,-36.9 218.459,-36.9 222.992,-41.4333 222.992,-45.9667 222.992,-45.9667 222.992,-55.0333 222.992,-55.0333 222.992,-59.5667 218.459,-64.1 213.925,-64.1 213.925,-64.1 168.067,-64.1 168.067,-64.1 163.533,-64.1 159,-59.5667 159,-55.0333 159,-55.0333 159,-45.9667 159,-45.9667 159,-41.4333 163.533,-36.9 168.067,-36.9\"></path> <text text-anchor=\"middle\" x=\"190.996\" y=\"-45.7\" font-family=\"Courier,monospace\" font-size=\"16.00\">Val 2</text> </g> <!-- node_1&#45;&gt;node_1_1 --> <g id=\"edge2\" class=\"edge\"><title>node_1-&gt;node_1_1</title> <path fill=\"none\" stroke=\"black\" d=\"M123.261,-50.5C133.651,-50.5 144.147,-50.5 153.642,-50.5\"></path> <polygon fill=\"black\" stroke=\"black\" points=\"153.807,-52.2501 158.807,-50.5 153.807,-48.7501 153.807,-52.2501\"></polygon> </g> <!-- node_1_2 --> <g id=\"node_1_2\" class=\"node\"><title>node_1_2</title> <path fill=\"#e6e6e6\" stroke=\"black\" stroke-width=\"0.5\" d=\"M268.059,-36.9C268.059,-36.9 313.917,-36.9 313.917,-36.9 318.451,-36.9 322.984,-41.4333 322.984,-45.9667 322.984,-45.9667 322.984,-55.0333 322.984,-55.0333 322.984,-59.5667 318.451,-64.1 313.917,-64.1 313.917,-64.1 268.059,-64.1 268.059,-64.1 263.525,-64.1 258.992,-59.5667 258.992,-55.0333 258.992,-55.0333 258.992,-45.9667 258.992,-45.9667 258.992,-41.4333 263.525,-36.9 268.059,-36.9\"></path> <text text-anchor=\"middle\" x=\"290.988\" y=\"-45.7\" font-family=\"Courier,monospace\" font-size=\"16.00\">Val 3</text> </g> <!-- node_1_1&#45;&gt;node_1_2 --> <g id=\"edge1\" class=\"edge\"><title>node_1_1-&gt;node_1_2</title> <path fill=\"none\" stroke=\"black\" stroke-width=\"0.6\" d=\"M223.001,-50.5C231.759,-50.5 241.407,-50.5 250.588,-50.5\"></path> <polygon fill=\"#404040\" stroke=\"black\" stroke-width=\"0.6\" points=\"250.848,-53.3001 258.848,-50.5 250.848,-47.7001 250.848,-53.3001\"></polygon> </g> <!-- node_0 --> <g id=\"node_0\" class=\"node\"><title>node_0</title> <polygon fill=\"#bfefff\" stroke=\"#000000\" stroke-width=\"0.42\" points=\"0,-70.5 0,-100.5 123,-100.5 123,-70.5 0,-70.5\"></polygon> <text text-anchor=\"middle\" x=\"61.5\" y=\"-81.1\" font-family=\"Courier,monospace\" font-size=\"16.00\">Key 1</text> </g> <!-- node_0_1 --> <g id=\"node_0_1\" class=\"node\"><title>node_0_1</title> <path fill=\"#e6e6e6\" stroke=\"black\" stroke-width=\"0.5\" d=\"M168.067,-71.9C168.067,-71.9 213.925,-71.9 213.925,-71.9 218.459,-71.9 222.992,-76.4333 222.992,-80.9667 222.992,-80.9667 222.992,-90.0333 222.992,-90.0333 222.992,-94.5667 218.459,-99.1 213.925,-99.1 213.925,-99.1 168.067,-99.1 168.067,-99.1 163.533,-99.1 159,-94.5667 159,-90.0333 159,-90.0333 159,-80.9667 159,-80.9667 159,-76.4333 163.533,-71.9 168.067,-71.9\"></path> <text text-anchor=\"middle\" x=\"190.996\" y=\"-80.7\" font-family=\"Courier,monospace\" font-size=\"16.00\">Val 1</text> </g> <!-- node_0&#45;&gt;node_0_1 --> <g id=\"edge3\" class=\"edge\"><title>node_0-&gt;node_0_1</title> <path fill=\"none\" stroke=\"black\" d=\"M123.261,-85.5C133.651,-85.5 144.147,-85.5 153.642,-85.5\"></path> <polygon fill=\"black\" stroke=\"black\" points=\"153.807,-87.2501 158.807,-85.5 153.807,-83.7501 153.807,-87.2501\"></polygon> </g> </g> </svg>",
          "nodes": [
               {
                    "id": "node_0",
                    "content": "Key 1",
                    "x": "50",
                    "y": "20",
                    "fillcolor": "#bfefff",
                    "textcolor": "white",
                    "strokecolor": "#FF0000",
                    "keyList": [
                         {
                              "id": "node_0_1",
                              "content": "Val 1",
                              "x": "50",
                              "y": "20",
                              "fillcolor": "#e6e6e6",
                              "textcolor": "white",
                              "strokecolor": "#FF0000"
                         }
                    ]
               },
               {
                    "id": "node_1",
                    "content": "Key 2",
                    "x": "50",
                    "y": "20",
                    "fillcolor": "#bfefff",
                    "textcolor": "white",
                    "strokecolor": "#FF0000",
                    "keyList": [
                         {
                              "id": "node_1_1",
                              "content": "Val 2",
                              "x": "50",
                              "y": "20",
                              "fillcolor": "#e6e6e6",
                              "textcolor": "white",
                              "strokecolor": "#FF0000"
                         },
                         {
                              "id": "node_1_2",
                              "content": "Val 3",
                              "x": "50",
                              "y": "20",
                              "fillcolor": "#e6e6e6",
                              "textcolor": "white",
                              "strokecolor": "#FF0000"
                         }
                    ]
               },
               {
                    "id": "node_2",
                    "content": "Key 3",
                    "x": "50",
                    "y": "20",
                    "fillcolor": "#bfefff",
                    "textcolor": "white",
                    "strokecolor": "#FF0000",
                    "keyList": []
               }
          ],
          "comp_id": "2lfog26JUeylAgoJCk4oK"
     },
     "iteration": 1,
     "hash": 5,
     "saveVersion": 2
}
    '''
    return "<h2>I'm a simple HashTable Component</h2>"
