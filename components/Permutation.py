from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Permutation")
def Permutation(content, session, headers, pageObj):
    '''
    {
     "type": "Permutation",
     "mode": "view",
     "content": {
          "version": "1.0",
          "options": [
               {
                    "blockType": "text",
                    "content": {
                         "data": "print \"Please enter the temperature in Celsius\"",
                         "mdhtml": "<p>print \u201cPlease enter the temperature in Celsius\u201d</p>\n"
                    },
                    "hashid": "zIqFzcpVTeLDG9J4SLAkN",
                    "maxRedemptionOfBlock": 1,
                    "locked": true,
                    "position": 0,
                    "linkedTo": null,
                    "duplicateBlockCount": 0
               },
               {
                    "blockType": "text",
                    "content": {
                         "data": "input temperatureC",
                         "mdhtml": "<p>input temperatureC</p>\n"
                    },
                    "hashid": "Oq4TUU8vbXgTZ-Iy4_v1C",
                    "maxRedemptionOfBlock": 1,
                    "locked": false,
                    "position": null,
                    "linkedTo": null,
                    "duplicateBlockCount": 0
               },
               {
                    "blockType": "text",
                    "content": {
                         "data": "temperatureF = (temperatureC * 9 / 5) + 32",
                         "mdhtml": "<p>temperatureF = (temperatureC * 9 / 5) + 32</p>\n"
                    },
                    "hashid": "mG0sHf2pbqtB-OEtrl0R8",
                    "maxRedemptionOfBlock": 1,
                    "locked": false,
                    "position": null,
                    "linkedTo": null,
                    "duplicateBlockCount": 0
               },
               {
                    "blockType": "text",
                    "content": {
                         "data": "print \"Temperature in Fahrenheit is :\"",
                         "mdhtml": "<p>print \u201cTemperature in Fahrenheit is :\u201d</p>\n"
                    },
                    "hashid": "evL1anA5LCjPZQ5Cvn-FT",
                    "maxRedemptionOfBlock": 1,
                    "locked": false,
                    "position": null,
                    "linkedTo": null,
                    "duplicateBlockCount": 0
               },
               {
                    "blockType": "text",
                    "content": {
                         "data": "print temperatureF",
                         "mdhtml": "<p>print temperatureF</p>\n"
                    },
                    "hashid": "5IkV-eRDQvDCQOpFwWEM2",
                    "maxRedemptionOfBlock": 1,
                    "locked": false,
                    "position": null,
                    "linkedTo": null,
                    "duplicateBlockCount": 0
               }
          ],
          "protected_content": [
               "zIqFzcpVTeLDG9J4SLAkN",
               "Oq4TUU8vbXgTZ-Iy4_v1C",
               "mG0sHf2pbqtB-OEtrl0R8",
               "evL1anA5LCjPZQ5Cvn-FT",
               "5IkV-eRDQvDCQOpFwWEM2"
          ],
          "numberOfQuestionBlock": 5,
          "question_statement": "Arrange the following instructions into the correct order.",
          "alignment": "Vertical",
          "showOptions": true,
          "disableSolution": false,
          "disableSubmit": false,
          "disableReset": false,
          "comp_id": "JCeUCWP6PTnY7Smx8Dwn2",
          "isCopied": true
     },
     "status": "normal",
     "contentID": "lVv_E_WD8QsGD7TZzW1h6",
     "widgetCopyId": "5825439251824640",
     "saveVersion": 2,
     "iteration": 15,
     "hash": 9,
     "children": [
          {
               "text": ""
          }
     ]
}
    '''
    return "<h2>I'm a simple Permutation Component</h2>"
