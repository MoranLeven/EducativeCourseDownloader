from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Sandpack")
def Sandpack(content, session, headers, pageObj):
    '''
    {
     "type": "Sandpack",
     "mode": "view",
     "content": {
          "version": 1,
          "showLineNumbers": true,
          "hideEditor": true,
          "hideConsole": true,
          "hideOutput": false,
          "hideTests": true,
          "hideStopBtn": true,
          "autoRun": true,
          "disableExecution": false,
          "codeHeight": 450,
          "outputHeight": 380,
          "directories": {},
          "primaryFile": "/package.json",
          "template": "vanilla",
          "selectedApiKeys": {},
          "caption": "",
          "files": {
               "/styles.css": {
                    "code": "body {\n  font-family: calibri;\n    line-height: 1.5;\n\n  -webkit-font-smoothing: auto;\n  -moz-font-smoothing: auto;\n  -moz-osx-font-smoothing: grayscale;\n  font-smoothing: auto;\n  text-rendering: optimizeLegibility;\n  font-smooth: always;\n  -webkit-tap-highlight-color: transparent;\n  -webkit-touch-callout: none;\n    font-size: 1.2rem;\n}\n#hint{\n  text-align: left;\n\n}\n#hint1{\n  text-align: left;\n\n}\n#hint2{\n  text-align: left;\n\n}\n#hint3{\n  text-align: left;\n\n}\n#hint4{\n  text-align: left;\n\n}\n#hint5{\n  text-align: left;\n\n}\n#hint6{\n  text-align: left;\n\n}\n#hint7{\n  text-align: left;\n\n}\n#hint8{\n  text-align: left;\n\n}\n#caretContainer{\n  margin-top: 10px;\n\n  background-color: #e5edfc;\n  max-width: 1000px;\n  min-height: 360px;\n}\n.container{\n\n}\n.caret{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret1{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret2{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret3{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret4{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret5{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret6{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret7{\n    width: 30px; /* Adjust the width as needed */\n\n}\n.caret8{\n    width: 30px; /* Adjust the width as needed */\n\n}\n#contentDiv{\n  width:680px;\n        background-color: #cffff1; /* Background color for table headings */\n\n}\n\n#content{\n  text-align: left; margin:5px;\n}\n#content1{\n  text-align: left; margin:5px;\n}\n#content2{\n  text-align: left; margin:5px;\n}\n#content3{\n  text-align: left; margin:5px;\n}\n#content31{\n  text-align: left; margin:5px; font-size: 1rem;\n}\n#content4{\n  text-align: left; margin:5px;\n}\n#content5{\n  text-align: left; margin:5px;\n}\n#content6{\n  text-align: left; margin:5px;\n}\n#content51{\n  text-align: left; margin:5px; font-size: 1rem;\n}\n#content61{\n  text-align: left; margin:5px; font-size: 1rem;\n}\n#content21{\n  text-align: left; margin:5px; font-size: 1rem;\n}\n#content11{\n  text-align: left; margin:5px; font-size: 1rem;\n}\n#content7{\n  text-align: left; margin:5px;\n}\n#content8{\n  text-align: left; margin:5px;\n}\nh1 {\n\n  font-size: 2.8rem;\n}\n/* Hide the paragraph by default */\n.hidden {\n  display: none;\n}\npre\n{\n  text-align: left;\n  line-height: 1.5;\n}",
                    "active": false,
                    "hidden": false,
                    "readOnly": false,
                    "visible": true,
                    "highlightedLines": ""
               },
               "/index.js": {
                    "code": "import \"./styles.css\";\n\nconst caret = document.getElementById('caret');\nconst content = document.getElementById('content');\nconst caret1 = document.getElementById('caret1');\nconst content1 = document.getElementById('content1');\nconst caret2 = document.getElementById('caret2');\nconst content2 = document.getElementById('content2');\nconst caret3 = document.getElementById('caret3');\nconst content3 = document.getElementById('content3');\nconst caret4 = document.getElementById('caret4');\nconst content4 = document.getElementById('content4');\nconst content31 = document.getElementById('content31');\nconst content41 = document.getElementById('content41');\nconst content5 = document.getElementById('content5');\nconst content51 = document.getElementById('content51');\nconst caret6 = document.getElementById('caret6');\nconst content6 = document.getElementById('content6');\nconst content61 = document.getElementById('content61');\nconst caret7 = document.getElementById('caret7');\nconst content7 = document.getElementById('content7');\nconst caret8 = document.getElementById('caret8');\nconst content8 = document.getElementById('content8');\ncaret.addEventListener('click', function() {\n  content.classList.toggle('hidden');\n  caret.textContent = content.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret1.addEventListener('click', function() {\n  content1.classList.toggle('hidden');\n  content11.classList.toggle('hidden');\n  caret1.textContent = content1.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret2.addEventListener('click', function() {\n  content2.classList.toggle('hidden');\n  content21.classList.toggle('hidden');\n  caret2.textContent = content2.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret3.addEventListener('click', function() {\n  content3.classList.toggle('hidden');\n  content31.classList.toggle('hidden');\n  caret3.textContent = content3.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret4.addEventListener('click', function() {\n  content4.classList.toggle('hidden');\n  caret4.textContent = content4.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret5.addEventListener('click', function() {\n  content5.classList.toggle('hidden');\n  content51.classList.toggle('hidden');\n  caret5.textContent = content5.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret6.addEventListener('click', function() {\n  content6.classList.toggle('hidden');\n  caret6.textContent = content6.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret7.addEventListener('click', function() {\n  content7.classList.toggle('hidden');\n  caret7.textContent = content7.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});\ncaret8.addEventListener('click', function() {\n  content8.classList.toggle('hidden');\n  caret8.textContent = content8.classList.contains('hidden') ? '\u25b6' : '\u25bc';\n});",
                    "active": false,
                    "hidden": false,
                    "readOnly": false,
                    "visible": true,
                    "highlightedLines": ""
               },
               "/index.html": {
                    "code": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>Spreadsheet vs Database</title>\n  <link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n  <center>\n  <div class=\"caret-container\" id=\"caretContainer\">\n    <p style=\"text-align: left; margin:5px;\"> Click the arrow to see the hint.\n    </p>\n      <p id =\"hint\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help with selecting specific columns in SQL?\n\n   &nbsp <button id=\"caret\" class=\"caret\">&#9658;</button>\n   </p>\n    <p id=\"content\" class=\"hidden\">\n      We use the SELECT query to retrieve data from the table. The data can be a single value, single row, single column, multiple rows, or multiple columns, depending on the constraints specified in the query. We can retrieve the data by specifying the column names in the query. We can also use *, which retrieves data from all columns.\n    <p></p>\n    </p>\n    \n    <p id =\"hint3\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help with setting an alias for a table in SQL?\n\n   &nbsp <button id=\"caret3\" class=\"caret3\">&#9658;</button>\n   </p>\n    <p id=\"content3\" class=\"hidden\">\n    Aliases are used to give a temporary name to tables or columns. An alias only exists for the duration of the query. Usually, the AS keyword is used for specifying an alias, but MySQL query can also work without the keyword. Following is the syntax that uses an alias for a table.\n    <pre id=\"content31\" class=\"hidden\" style=\"text-align: left\">\n    SELECT t.ColumnName\n    FROM   TableName AS t;</pre>\n    </p>\n    <p id =\"hint4\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help understanding a JOIN operation?\n\n   &nbsp <button id=\"caret4\" class=\"caret4\">&#9658;</button>\n   </p>\n    <p id=\"content4\" class=\"hidden\">\n    The JOIN operation combines rows from two or more tables based on their related columns.\n    <p></p>\n    </p>\n    <p id =\"hint2\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help with aggregate functions?\n\n   &nbsp <button id=\"caret2\" class=\"caret2\">&#9658;</button>\n   </p>\n    <p id=\"content2\" class=\"hidden\">\n    The aggregate functions perform calculations on a set of values and return a single value with the summarized data. The aggregate functions are SUM, AVG, MIN, MAX, and COUNT. The following is the syntax of the aggregate functions:\n    <pre id=\"content21\" class=\"hidden\" style=\"text-align: left\">\n    SELECT   Aggregate_function(ColumnName)\n    FROM     TableName\n    [WHERE   condition];</pre>\n    </p>\n<p id =\"hint5\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help with grouping the records in a table?\n\n   &nbsp <button id=\"caret5\" class=\"caret5\">&#9658;</button>\n   </p>\n    <p id=\"content5\" class=\"hidden\">\n    The GROUP BY clause creates the groups based on the data. It is often used with aggregate functions like SUM, AVG, MIN, MAX, and COUNT. The following is the syntax of the GROUP BY clause:\n    <pre id=\"content51\" class=\"hidden\" style=\"text-align: left\">\n    SELECT   ColumnName(s)\n    FROM     TableName\n    GROUP BY ColumnName(s);</pre>\n    </p>\n    <p id =\"hint1\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help understanding the HAVING clause in SQL?\n\n   &nbsp <button id=\"caret1\" class=\"caret1\">&#9658;</button>\n   </p>\n    <p id=\"content1\" class=\"hidden\">\n    The HAVING clause in SQL is used to filter groups of records after they have been grouped by the GROUP BY clause. The conditions are applied on the aggregate functions like SUM, AVG, COUNT, etc.\n    <pre id=\"content11\" class=\"hidden\" style=\"text-align: left\">\n    SELECT   Column1, aggregate_function(Column2)\n    FROM     TableName\n    GROUP BY Column1\n    HAVING   aggregate_condition;</pre>\n    </p>\n    <p id =\"hint6\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help with filtering the data?\n\n   &nbsp <button id=\"caret6\" class=\"caret6\">&#9658;</button>\n   </p>\n    <p id=\"content6\" class=\"hidden\">\n    The WHERE clause specifies the conditions on which we want to retrieve the records. We can use equality operators, relational operators, logical operators, or a combination of any of these in the condition.\n    <p></p>\n    </p>\n    <p id =\"hint7\" style=\"margin:5px;\"><strong>Hint:</strong> Do you need help understanding a nested subquery in SQL?\n\n   &nbsp <button id=\"caret7\" class=\"caret7\">&#9658;</button>\n   </p>\n    <p id=\"content7\" class=\"hidden\">\n    A query within a query is called a subquery. A subquery must be enclosed in parentheses. A subquery within a subquery is referred to as a nested subquery.\n        <p></p>\n</p>\n    <p id =\"hint8\" style=\"margin:5px;\"><strong>Hint:</strong> How can a subquery be utilized in SQL?\n\n   &nbsp <button id=\"caret8\" class=\"caret8\">&#9658;</button>\n   </p>\n    <p id=\"content8\" class=\"hidden\">\n    A subquery can be used with CRUD operations like SELECT, INSERT, UPDATE, and DELETE. It can also be used with other clauses like the FROM and WHERE clauses. We can also use a subquery within a condition for comparison, but it must be written on the right side of the operator or the clause.\n    <p></p></p>\n  </div>\n\n  <script src=\"script.js\"></script>\n</body>\n</html>\n",
                    "active": false,
                    "hidden": false,
                    "readOnly": false,
                    "visible": true,
                    "highlightedLines": ""
               },
               "/package.json": {
                    "code": "{\n\t\"dependencies\": {},\n\t\"main\": \"/index.js\"\n}",
                    "active": true,
                    "hidden": false,
                    "readOnly": false,
                    "visible": true,
                    "highlightedLines": ""
               }
          },
          "comp_id": "y7ACZnNrd8REs9acWF_Rj",
          "isCopied": true
     },
     "status": "normal",
     "contentID": "2quPPHDWHuyXmKysSvT4e",
     "saveVersion": 35,
     "widgetCopyId": "6752811677515776",
     "iteration": 11,
     "hash": 10,
     "children": [
          {
               "text": ""
          }
     ]
}
    '''
    return "<h2>I'm a simple Sandpack Component</h2>"
