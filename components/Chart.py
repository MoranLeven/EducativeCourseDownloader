from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Chart")
def Chart(content, session, headers, pageObj):
    '''
    {
     "type": "Chart",
     "mode": "view",
     "content": {
          "config": "{\n  \"type\": \"line\",\n  \"data\": {\n    \"labels\": [\n      \"2011\",\n      \"2015\",\n      \"2016\",\n      \"2017\",\n      \"2018\",\n      \"2020\"\n    ],\n    \"datasets\": [\n      {\n        \"label\": \"Number of WhatsApp messages sent globally per day\",\n        \"borderColor\": \"rgb(230,0,0)\",\n        \"data\": [\n          \"1\",\n          \"30\",\n          \"42\",\n          \"55\",\n          \"65\",\n          \"100\"\n        ]\n      }\n    ]\n  },\n  \"options\": {\n    \"responsive\": true,\n    \"title\": {\n      \"display\": true,\n      \"text\": \"WhatsApp messages per day [source: WhatsApp]\"\n    },\n    \"tooltips\": {\n      \"mode\": \"index\"\n    },\n    \"hover\": {\n      \"mode\": \"index\"\n    },\n    \"scales\": {\n      \"xAxes\": [\n        {\n          \"scaleLabel\": {\n            \"display\": true,\n            \"labelString\": \"Year\"\n          }\n        }\n      ],\n      \"yAxes\": [\n        {\n          \"stacked\": false,\n          \"scaleLabel\": {\n            \"display\": true,\n            \"labelString\": \"Billion\"\n          }\n        }\n      ]\n    }\n  }\n}",
          "type": "line",
          "comp_id": "B5zJ3_f9pH8xlEyglbzjI",
          "caption": "Number of WhatsApp messages sent per day"
     },
     "status": "normal",
     "contentID": "Z4cIJj-robrxa0LSSuGhH",
     "saveVersion": 1,
     "widgetCopyId": "4852320184827904",
     "iteration": 0,
     "hash": 1,
     "children": [
          {
               "text": ""
          }
     ]
}
    '''
    return "<h2>I'm a simple Chart Component</h2>"
