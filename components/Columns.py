from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Columns")
def Columns(content, session, headers, pageObj):
    # Extract the pre-rendered HTML block containing the columns
    raw_html = content.get("html", "")
    
    if not raw_html:
        return ""
        
    return f"""
    <div class="widget columns-widget" style="display: flex; flex-wrap: wrap; gap: 20px; width: 100%;">
        <div style="flex: 1; min-width: 300px;">
            {raw_html}
        </div>
    </div>
    """