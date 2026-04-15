from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("TableHTML")
def TableHTML(content, session, headers, pageObj):
    # Educative provides the full HTML for the table directly in the JSON
    raw_html = content.get("html", "")
    
    if not raw_html:
        return ""
        
    html = f"""
    <div class="widget table-widget">
        <div class="widget-body" style="overflow-x: auto;">
            {raw_html}
        </div>
    </div>
    """
    return html