from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("QuizViewer")
def QuizViewer(content, session, headers, pageObj):
    '''
    {
     "type": "QuizViewer",
     "content": {
          "type": "QuizV2",
          "comp_id": "Sb-qIl5C36cRTPb4psFFi",
          "dynamicQuestions": null,
          "quizTitle": "Test your knowledge!",
          "children": [
               {
                    "type": "QuizQuestion",
                    "questionType": "SINGLE_SELECTION",
                    "correctAnswers": [
                         "5ysfrczznLrpLATltE5_p"
                    ],
                    "dataKey": "aIzNcUSC5xbKe7TqG89j9",
                    "children": [
                         {
                              "type": "QuestionTitle",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "In data parallelism, what is the function of a parameter server?"
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionOptions",
                              "children": [
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "b9cealP98vLRRENg7h1bj",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "To perform local updates on a single GPU"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "5ysfrczznLrpLATltE5_p",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "To aggregate and distribute model parameters for workers"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "N4nvbo1hBSO4XCoD5iA4g",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "To preprocess the data"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "NMJiMEabhkSPG066jJhfS",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "To train a backup model for fault tolerance"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionExplanation",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "The parameter server acts as the central ground truth, aggregating gradients and updating the training servers with the new model weights on each iteration."
                                             }
                                        ]
                                   }
                              ]
                         }
                    ]
               },
               {
                    "type": "QuizQuestion",
                    "questionType": "SINGLE_SELECTION",
                    "correctAnswers": [
                         "6Vu7nT-0W3FhxumqSzBeI"
                    ],
                    "dataKey": "MuyLd7_7L17-t8eVvi-Hb",
                    "children": [
                         {
                              "type": "QuestionTitle",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "In model parallelism, how is the model typically divided?"
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionOptions",
                              "children": [
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "6qcvQceJ7ZAEPn2KcVfzB",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "By slicing the dataset across GPUs"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "crY3_fx4Fmlay9Rtvm0XH",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "By using pretrained models for some layers"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "1s20uQmsVGDY4VEyEhGGZ",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "By running independent models on different GPUs"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "6Vu7nT-0W3FhxumqSzBeI",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "By splitting layers or operations across different GPUs"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionExplanation",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "In model parallelism, we split up the model into multiple chunks, which are computed by separate GPUs."
                                             }
                                        ]
                                   }
                              ]
                         }
                    ]
               },
               {
                    "type": "QuizQuestion",
                    "questionType": "SINGLE_SELECTION",
                    "correctAnswers": [
                         "lmf3xWTGDCT3PyDg0dp9b"
                    ],
                    "dataKey": "5QH6mFNvd5XJC3BUDDed9",
                    "children": [
                         {
                              "type": "QuestionTitle",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "A team is training a transformer model with 10 billion parameters. Due to the GPU memory limit, they cannot fit the model on a single GPU. Which parallelism technique is most suitable for this scenario?"
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionOptions",
                              "children": [
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "_3GFxX7c0qQ-NYVAXxmDw",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "Data parallelism "
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "zFEhVRC1VkzCZsEnU98QV",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "Model parallelism"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "lmf3xWTGDCT3PyDg0dp9b",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "Hybrid parallelism"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   },
                                   {
                                        "type": "QuestionOption",
                                        "dataKey": "JF2A0C2yLFXrJnttddLmd",
                                        "children": [
                                             {
                                                  "type": "OptionContent",
                                                  "children": [
                                                       {
                                                            "type": "paragraph",
                                                            "children": [
                                                                 {
                                                                      "text": "Single-node training"
                                                                 }
                                                            ]
                                                       }
                                                  ]
                                             }
                                        ]
                                   }
                              ]
                         },
                         {
                              "type": "QuestionExplanation",
                              "children": [
                                   {
                                        "type": "paragraph",
                                        "children": [
                                             {
                                                  "text": "A 10-billion parameter transformer model exceeds the memory capacity of a single GPU, necessitating a strategy that distributes the model itself across multiple GPUs. Hybrid parallelism addresses this by combining model parallelism and data parallelism. Model parallelism splits the model into smaller parts, allowing it to fit across multiple GPUs. Simultaneously, data parallelism feeds different portions of the data to each GPU, enabling them to work concurrently on different aspects of the training process. This dual approach overcomes memory constraints and accelerates training through parallel computation."
                                             }
                                        ]
                                   }
                              ]
                         }
                    ]
               }
          ]
     },
     "hash": 25
}
    '''
    return "<h2>I'm a simple QuizViewer Component</h2>"
