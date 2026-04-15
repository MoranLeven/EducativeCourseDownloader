from ..componentregistry import ComponentRegistry
from .computilities import clean_html
@ComponentRegistry.register("MarkdownEditor")
def MarkdownEditor(content, session, headers, pageObj):
    '''
    {
     "type": "MarkdownEditor",
     "mode": "edit",
     "content": {
          "version": "2.0",
          "text": "This figure shows the Chrome browser displaying the `index.html` file with the canvas, which has the check mark that was drawn by our Kotlin code, running within the WASM virtual machine.\n\n___",
          "mdHtml": "<p>This figure shows the Chrome browser displaying the <code>index.html</code> file with the canvas, which has the check mark that was drawn by our Kotlin code, running within the WASM virtual machine.</p>\n<hr />\n",
          "comp_id": "977e36d3-5ff2-42fb-bdc7-d986517231dc"
     },
     "hash": "8",
     "saveVersion": 1,
     "iteration": 0
}
    '''
    rawMarkdown = content.get('mdHtml',"") or content.get("text","")
    html = f'<div class="markdown-body">{clean_html(rawMarkdown)}</div>'
    return html
