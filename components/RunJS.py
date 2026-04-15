from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("RunJS")
def RunJS(content, session, headers, pageObj):
    '''
    {
     "type": "RunJS",
     "mode": "edit",
     "content": {
          "version": "11",
          "filename": "",
          "active": "html",
          "jotted": {
               "pane": "result",
               "height": "500px",
               "heightCodepanel": null,
               "showBlank": false,
               "hints": null,
               "hideResult": false,
               "hideHtml": true,
               "hideCss": true,
               "hideJs": true,
               "hideNav": true,
               "showBabelTransformPane": false,
               "codePlaygroundTemplate": "jottedTabs",
               "showLineNumbers": true,
               "autoRun": true,
               "runOnLoad": false,
               "theme": "default",
               "exercise": false,
               "showSolution": false,
               "disableScss": true,
               "caption": "",
               "toggleState": {
                    "result": true,
                    "html": true,
                    "css": true,
                    "js": true
               },
               "readOnlyState": {
                    "html": false,
                    "css": false,
                    "js": false
               },
               "solutionPanels": {
                    "js": "",
                    "html": "",
                    "css": ""
               },
               "panelsHighlightedLines": {
                    "js": "",
                    "html": "",
                    "css": "",
                    "hiddenjs": ""
               },
               "plugins": [
                    {
                         "name": "codemirror",
                         "options": {
                              "lineNumbers": true
                         }
                    }
               ],
               "files": [
                    {
                         "type": "css",
                         "content": ".hidden{\n    display: none;\n}\n\nbody.dark{\n background-color: #333333;\n color: white;\n}\n\nheader{\n    text-align: center;\n    padding-bottom: 10px;\n    border-bottom: 1px solid white;\n}\n\nbutton {\n    justify-self: center;\n}\n\n#game{\n    display: flex;\n    justify-content: center;\n}\n\n#number-container > p{\n    border: 1px solid black;\n    border-radius: 15px;\n    width: 50px;\n    height: 50px;\n    font-size: 30pt;\n    margin-left: 50px;\n    margin-right: 5px;\n    margin-bottom: 5px;\n    text-align: center;\n}\n\n#board{\n    padding-top: 10px;\n    margin-top: 10px;\n    display: flex;\n    flex-wrap: wrap;\n    justify-content: center;\n    align-content: flex-start;\n    width: 250px;\n    height: 250px;\n}\n\n.tile {\n    border: 1px solid black;\n    width: 50px;\n    height: 50px;\n    text-align: center;\n    margin: 0px;\n    vertical-align: middle;\n    font-size: 30pt;\n}\n\np.selected {\n    background-color: lightblue;\n}\n\np.incorrect{\n    color: red;\n}\n\n.rightBorder {\n  border-right: 4px solid black;\n}\n\n.bottomBorder{\n    border-bottom: 4px solid black;\n}\n"
                    },
                    {
                         "type": "exercise",
                         "content": "var TestResult = function() {\r\n  this.succeeded = false;\r\n  this.reason = \"\";\r\n  this.input = \"\";\r\n  this.expected_output = \"\";\r\n  this.actual_output = \"\";\r\n};\r\n\r\nvar executeTests = function(\r\n  userJsCode,\r\n  userCssCode,\r\n  userHtmlCode,\r\n  userHtmlPage\r\n) {\r\n  var results = [];\r\n\r\n  const jsdom = require(\"jsdom\");\r\n  const { JSDOM } = jsdom;\r\n  const dom2 = new JSDOM(userHtmlPage, { runScripts: \"dangerously\" });\r\n\r\n  const pTag = dom2.window.document.querySelector(\"p\");\r\n\r\n  const result = new TestResult();\r\n  result.expected_output = \"Hello World\";\r\n  result.input = \"Html page\";\r\n\r\n  if (!pTag) {\r\n    result.actual_output = \"null\";\r\n    result.succeeded = false;\r\n    result.reason = \"No p tag found\";\r\n  } else {\r\n    const pTagText = pTag ? pTag.textContent : \"\";\r\n    result.actual_output = pTagText;\r\n    if (pTagText.trim() != \"Hello World\") {\r\n      result.reason = \"Expected output (Hello World in a p tag) did not match\";\r\n      result.succeeded = false;\r\n    } else {\r\n      result.succeeded = true;\r\n      result.reason = \"Found p tag with Hello World\";\r\n    }\r\n  }\r\n\r\n  results.push(result);\r\n\r\n  return results;\r\n};\r\n\r\n// Async Tests Example\r\n/*\r\nvar executeTestsAsync = function(\r\n  userJsCode,\r\n  userCssCode,\r\n  userHtmlCode,\r\n  userHtmlPage\r\n) {\r\n  var results = [];\r\n  return new Promise(resolve => {\r\n\r\n    const jsdom = require(\"jsdom\");\r\n    const { JSDOM } = jsdom;\r\n    const dom2 = new JSDOM(userHtmlPage, { runScripts: \"dangerously\" });\r\n\r\n    if (!dom2.window.onModulesLoaded) {\r\n      console.log(\"window.onModulesLoaded not found!\");\r\n    \tresolve(results);\r\n    }\r\n    dom2.window.onModulesLoaded.then(()=>{\r\n      const pTag = dom2.window.document.querySelector(\"p\");\r\n\r\n      const result = new TestResult();\r\n      result.expected_output = \"Hello World\";\r\n      result.input = \"Html page\";\r\n\r\n      if (!pTag) {\r\n        result.actual_output = \"null\";\r\n        result.succeeded = false;\r\n        result.reason = \"No p tag found\";\r\n      } else {\r\n        const pTagText = pTag ? pTag.textContent : \"\";\r\n        result.actual_output = pTagText;\r\n        if (pTagText.trim() != \"Hello World\") {\r\n          result.reason = \"Expected output (Hello World in a p tag) did not match\";\r\n          result.succeeded = false;\r\n        } else {\r\n          result.succeeded = true;\r\n          result.reason = \"Found p tag with Hello World\";\r\n        }\r\n      }\r\n\r\n      results.push(result);\r\n      resolve(results);\r\n    });\r\n  });\r\n};\r\n*/"
                    },
                    {
                         "type": "hiddenjs",
                         "content": "\n\n"
                    },
                    {
                         "type": "html",
                         "content": "<!DOCTYPE html>\r\n<html>\r\n <head>\r\n     <meta charset=\"utf-8\"/>\r\n     <title>Sudoku Game</title>\r\n     <link rel=\"stylesheet\" href=\"style.css\">\r\n     <script src=\"index.js\"></script>\r\n </head>\r\n <header>\r\n     <h1>Sudoku</h1>\r\n     <button id=\"start-btn\">Create new game</button>\r\n </header>\r\n <body class=\"dark\">\r\n  <div id=\"game\">\r\n      <div id=\"board\"></div>\r\n      <div id=\"number-container\" class=\"hidden\">\r\n          <p id=\"one\">1</p>\r\n          <p id=\"two\">2</p>\r\n          <p id=\"three\">3</p>\r\n          <p id=\"four\">4</p>\r\n      </div>\r\n  </div>\r\n  <div>\r\n  </div>\r\n </body>\r\n <footer>\r\n\r\n </footer>\r\n</html>"
                    },
                    {
                         "type": "js",
                         "content": "const values = [\"--4-4-3--4-3-1--\",\"1342423124133124\"];\r\n\r\nvar selectedNum;\r\nvar selectedTile;\r\nvar disableSelect;\r\n\r\nwindow.onload = function(){\r\n id(\"start-btn\").addEventListener(\"click\", Game);\r\n for (let i=0;i<id(\"number-container\").children.length; i++){\r\n    id(\"number-container\").children[i].addEventListener(\"click\", function(){\r\n        if(!disableSelect){\r\n        if(this.classList.contains(\"selected\")){\r\n            this.classList.remove(\"selected\");\r\n            selectedNum = null;\r\n        } else{\r\n            for(let i=0; i<4; i++){\r\n                id(\"number-container\").children[i].classList.remove(\"selected\");\r\n            }\r\n            this.classList.add(\"selected\");\r\n            selectedNum = this;\r\n            updateMove();\r\n        }\r\n    }\r\n    });\r\n}\r\n}\r\n\r\n\r\nfunction Game(){\r\n    if(id(\"start-btn\").innerHTML == \"Create new game\"){\r\n        id(\"start-btn\").innerHTML = \"Submit game\";\r\n        let board;\r\n        board = values[0];\r\n        disableSelect = false;\r\n        generateBoard(board);\r\n        id(\"number-container\").classList.remove(\"hidden\");\r\n    } else if(id(\"start-btn\").innerHTML == \"Submit game\"){\r\n        id(\"start-btn\").innerHTML = \"Create new game\";\r\n        endGame();\r\n    }\r\n    \r\n}\r\n\r\nfunction generateBoard(board){\r\n    clearPrevious();\r\n    let idCount = 0;\r\n    for(let i =0; i<16; i++){\r\n        let tile = document.createElement(\"p\");\r\n        if(board.charAt(i) != \"-\"){\r\n            tile.textContent = board.charAt(i);\r\n        }else {\r\n            tile.textContent = \"\";\r\n            tile.addEventListener(\"click\",function(){\r\n                if(!disableSelect){\r\n                if(tile.classList.contains(\"selected\")){\r\n                    tile.classList.remove(\"selected\");\r\n                    selectedTile = null;\r\n                } else{\r\n                    for(let i=0; i<16; i++){\r\n                        qsa(\".tile\")[i].classList.remove(\"selected\");\r\n                    }\r\n                    tile.classList.add(\"selected\");\r\n                    selectedTile = tile;\r\n                    updateMove();\r\n                }\r\n            }\r\n            });\r\n        }\r\n        tile.id = idCount;\r\n        idCount++;\r\n        tile.classList.add(\"tile\");\r\n        if(tile.id > 3 && tile.id < 8){\r\n            tile.classList.add(\"bottomBorder\");\r\n        }\r\n        if(tile.id % 4 == 1 ){\r\n            tile.classList.add(\"rightBorder\");\r\n        }\r\n        id(\"board\").appendChild(tile);\r\n    }\r\n}\r\n\r\nfunction updateMove(){\r\n    if(selectedTile && selectedNum){\r\n        selectedTile.textContent = selectedNum.textContent;\r\n        if(checkCorrect(selectedTile)){\r\n            selectedTile.classList.remove(\"selected\");\r\n            selectedTile = null;\r\n        } else{\r\n            disableSelect = true;\r\n            selectedTile.classList.add(\"incorrect\");\r\n            setTimeout(function(){\r\n                disableSelect = false;\r\n                selectedTile.classList.remove(\"incorrect\");\r\n                selectedTile.classList.remove(\"selected\");\r\n                selectedTile.textContent = \"\";\r\n                selectedTile = null;\r\n            }, 1000);\r\n        }\r\n    }\r\n}\r\n\r\nfunction checkCorrect(tile){\r\n    let solution;\r\n    solution = values[1];\r\n    if(solution.charAt(tile.id) == tile.textContent) return true;\r\n    else return false;\r\n}\r\n\r\nfunction endGame(){\r\n    let solution;\r\n    solution = values[1];\r\n    disableSelect = true;\r\n    for(let i=0; i< 16; i++){\r\n        if(qsa(\".tile\")[i].textContent != solution.charAt(i)){\r\n            qsa(\".tile\")[i].textContent = solution.charAt(i);\r\n            qsa(\".tile\")[i].classList.add(\"selected\");\r\n        }\r\n    }\r\n    for (let i=0;i<id(\"number-container\").children.length; i++){\r\n        id(\"number-container\").children[i].classList.remove(\"selected\");\r\n    }\r\n    selectedTile = null;\r\n    selectedNum = null;\r\n}\r\nfunction clearPrevious(){\r\n    let tiles = qsa(\".tile\");\r\n    for(let i=0; i<tiles.length; i++){\r\n        tiles[i].remove();\r\n    }\r\n\r\n    for (let i=0;i<id(\"number-container\").children.length; i++){\r\n        id(\"number-container\").children[i].classList.remove(\"selected\");\r\n    }\r\n    selectedTile = null;\r\n    selectedNum = null;\r\n}\r\n\r\nfunction qs(selector) {\r\n    return document.querySelector(selector);\r\n}\r\n\r\nfunction qsa(selector) {\r\n    return document.querySelectorAll(selector);\r\n}\r\nfunction id(id){\r\n    return document.getElementById(id);\r\n}"
                    }
               ]
          },
          "selectedApiKeys": {},
          "plugins": [
               {
                    "name": "codemirror",
                    "options": {
                         "lineNumbers": true,
                         "theme": "default"
                    }
               }
          ],
          "comp_id": "_08ER_rkYL_eISa6nth76"
     },
     "iteration": 1,
     "hash": 2,
     "saveVersion": 6,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "HeA5ODQ1LQD9vjpGKvMEL"
}
    '''
    return "<h2>I'm a simple RunJS Component</h2>"
