from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Matrix")
def Matrix(content, session, headers, pageObj):
    '''
    {
     "type": "Matrix",
     "mode": "view",
     "content": {
          "version": "2.0",
          "caption": "Sample Output Array",
          "svg_string": "<svg id=\"SvgjsSvg1001\" width=\"144\" height=\"144\" xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:svgjs=\"http://svgjs.com/svgjs\" viewBox=\"0 0 144 144\"><defs id=\"SvgjsDefs1002\"></defs><svg id=\"SvgjsSvg1008\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1009\" width=\"40\" height=\"40\" x=\"10\" y=\"10\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1010\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"23.6484375\" y=\"38\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">0</text></svg><svg id=\"SvgjsSvg1011\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1012\" width=\"40\" height=\"40\" x=\"10\" y=\"53\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1013\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"19.1015625\" y=\"81\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">-1</text></svg><svg id=\"SvgjsSvg1014\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1015\" width=\"40\" height=\"40\" x=\"10\" y=\"96\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1016\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"19.1015625\" y=\"124\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">-1</text></svg><svg id=\"SvgjsSvg1017\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1018\" width=\"40\" height=\"40\" x=\"53\" y=\"10\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1019\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"66.6484375\" y=\"38\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">1</text></svg><svg id=\"SvgjsSvg1020\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1021\" width=\"40\" height=\"40\" x=\"53\" y=\"53\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1022\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"66.6484375\" y=\"81\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">0</text></svg><svg id=\"SvgjsSvg1023\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1024\" width=\"40\" height=\"40\" x=\"53\" y=\"96\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1025\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"62.1015625\" y=\"124\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">-1</text></svg><svg id=\"SvgjsSvg1026\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1027\" width=\"40\" height=\"40\" x=\"96\" y=\"10\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1028\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"109.6484375\" y=\"38\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">1</text></svg><svg id=\"SvgjsSvg1029\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1030\" width=\"40\" height=\"40\" x=\"96\" y=\"53\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1031\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"109.6484375\" y=\"81\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">1</text></svg><svg id=\"SvgjsSvg1032\" style=\"overflow: visible;\"><rect id=\"SvgjsRect1033\" width=\"40\" height=\"40\" x=\"96\" y=\"96\" fill=\"#caff97\" fill-opacity=\"1\" rx=\"3\" ry=\"3\" stroke-opacity=\"1\" stroke=\"#000000\" stroke-width=\"1\"></rect><text id=\"SvgjsText1034\" font-family=\"Verdana\" font-size=\"20\" size=\"20\" family=\"Verdana\" x=\"109.6484375\" y=\"124\" svgjs:data=\"{&quot;leading&quot;:&quot;1.3&quot;}\">0</text></svg></svg>",
          "svg_width": 144,
          "svg_height": 144,
          "matrix_data": {
               "width": 144,
               "height": 144,
               "top_padding": 10,
               "right_padding": 10,
               "cell_right_padding": 5,
               "row_gap": 3,
               "cols": [
                    {
                         "max_width": 40,
                         "cells": [
                              {
                                   "text": "0",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "-1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "-1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              }
                         ]
                    },
                    {
                         "max_width": 40,
                         "cells": [
                              {
                                   "text": "1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "0",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "-1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              }
                         ]
                    },
                    {
                         "max_width": 40,
                         "cells": [
                              {
                                   "text": "1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "1",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              },
                              {
                                   "text": "0",
                                   "width": 40,
                                   "height": 40,
                                   "color": "#caff97"
                              }
                         ]
                    }
               ],
               "minimum_cell_height": 40,
               "cell_left_padding": 5,
               "col_gap": 3,
               "version": 1,
               "left_padding": 10,
               "minimum_cell_width": 40,
               "bottom_padding": 10
          },
          "comp_id": "862c821c-9e61-41ca-80d3-a9925040ef96"
     },
     "hash": 1,
     "iteration": 0,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal"
}
    '''
    return "<h2>I'm a simple Matrix Component</h2>"
