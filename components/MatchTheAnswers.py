from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("MatchTheAnswers")
def MatchTheAnswers(content, session, headers, pageObj):
    '''
    {
     "type": "MatchTheAnswers",
     "mode": "edit",
     "content": {
          "version": "1.0",
          "content": {
               "statements": [
                    [
                         {
                              "left": {
                                   "text": "Our server code needs to process incoming requests. This processing is sequential and includes authentication, authorization, data sanitization, forwarding to the appropriate server for load balancing, and finally returning the result.",
                                   "mdHtml": "<p>Our server code needs to process incoming requests. This processing is sequential and includes authentication, authorization, data sanitization, forwarding to the appropriate server for load balancing, and finally returning the result.</p>\n"
                              },
                              "right": {
                                   "text": "Strategy",
                                   "mdHtml": "<p>Strategy</p>\n"
                              },
                              "explanation": ""
                         },
                         {
                              "left": {
                                   "text": "Our code needs to go over the information of all the students in a class arranged as a binary search tree.",
                                   "mdHtml": "<p>Our code needs to go over the information of all the students in a class arranged as a binary search tree.</p>\n"
                              },
                              "right": {
                                   "text": "Mediator",
                                   "mdHtml": "<p>Mediator</p>\n"
                              },
                              "explanation": ""
                         },
                         {
                              "right": {
                                   "text": "State",
                                   "mdHtml": "<p>State</p>\n"
                              },
                              "left": {
                                   "text": "There\u2019s a web page that has $N$ components that might need to communicate with each other. We have to prevent such tight coupling.",
                                   "mdHtml": "<p>There\u2019s a web page that has <span class=\"katex\"><span class=\"katex-mathml\"><math xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>N</mi></mrow><annotation encoding=\"application/x-tex\">N</annotation></semantics></math></span><span class=\"katex-html\" aria-hidden=\"true\"><span class=\"base\"><span class=\"strut\" style=\"height:0.6833em;\"></span><span class=\"mord mathnormal\" style=\"margin-right:0.10903em;\">N</span></span></span></span> components that might need to communicate with each other. We have to prevent such tight coupling.</p>\n"
                              }
                         },
                         {
                              "right": {
                                   "text": "Iterator",
                                   "mdHtml": "<p>Iterator</p>\n"
                              },
                              "left": {
                                   "text": "We\u2019re creating a text editor application that allows the user to write text, edit it, and undo changes.",
                                   "mdHtml": "<p>We\u2019re creating a text editor application that allows the user to write text, edit it, and undo changes.</p>\n"
                              }
                         },
                         {
                              "right": {
                                   "text": "Memento",
                                   "mdHtml": "<p>Memento</p>\n"
                              },
                              "left": {
                                   "text": "There\u2019s a web page that has $N$ components. When one component has information to share, only those other components that require this information would be updated. Other components won't have access to this newly available information.",
                                   "mdHtml": "<p>There\u2019s a web page that has <span class=\"katex\"><span class=\"katex-mathml\"><math xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>N</mi></mrow><annotation encoding=\"application/x-tex\">N</annotation></semantics></math></span><span class=\"katex-html\" aria-hidden=\"true\"><span class=\"base\"><span class=\"strut\" style=\"height:0.6833em;\"></span><span class=\"mord mathnormal\" style=\"margin-right:0.10903em;\">N</span></span></span></span> components. When one component has information to share, only those other components that require this information would be updated. Other components won\u2019t have access to this newly available information.</p>\n"
                              }
                         },
                         {
                              "right": {
                                   "text": "Observer",
                                   "mdHtml": "<p>Observer</p>\n"
                              },
                              "left": {
                                   "text": "When the phone is locked, the screen should show the keypad for entering the pin code.\nIf the phone is unlocked, the screen should show the home screen with access to all the apps.\n",
                                   "mdHtml": "<p>When the phone is locked, the screen should show the keypad for entering the pin code.\nIf the phone is unlocked, the screen should show the home screen with access to all the apps.</p>\n"
                              }
                         },
                         {
                              "left": {
                                   "text": "We need to create a program that encrypts data. We can use different algorithms such as AES, DES, RSA, etc.",
                                   "mdHtml": "<p>We need to create a program that encrypts data. We can use different algorithms such as AES, DES, RSA, etc.</p>\n"
                              },
                              "right": {
                                   "text": "Chain of Responsibility",
                                   "mdHtml": "<p>Chain of Responsibility</p>\n"
                              }
                         }
                    ]
               ]
          },
          "protectedContent": {
               "answers": [
                    [
                         6,
                         3,
                         1,
                         4,
                         5,
                         2,
                         0
                    ]
               ]
          },
          "actualAnswers": {
               "answers": [
                    [
                         6,
                         3,
                         1,
                         4,
                         5,
                         2,
                         0
                    ]
               ]
          },
          "comp_id": "f4OEMt-OxcQKovoJMrVvx"
     },
     "iteration": 0,
     "hash": 1,
     "children": [
          {
               "text": ""
          }
     ],
     "status": "normal",
     "contentID": "Wi7wpggnvsnkXCwqXMFCB",
     "saveVersion": 2
}
    '''
    return "<h2>I'm a simple MatchTheAnswers Component</h2>"
