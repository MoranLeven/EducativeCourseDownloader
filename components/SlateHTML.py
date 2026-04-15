from ..componentregistry import ComponentRegistry
from .computilities import clean_html

@ComponentRegistry.register("SlateHTML")
def SlateHTML(content, session, headers,pageObj):

    html = clean_html(content.get('html'))
    return html
