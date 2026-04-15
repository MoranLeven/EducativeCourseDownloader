from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("SpoilerEditor")
def SpoilerEditor(content, session, headers, pageObj):
    # Extract the hidden HTML content and the button text
    mdHtml = content.get("mdHtml", "")
    showHintText = content.get("showHintText", "Show Hint")
    
    html = f"""
    <div class="widget spoiler-widget">
        <details>
            <summary class="spoiler-btn">{showHintText}</summary>
            <div class="spoiler-content">
                {mdHtml}
            </div>
        </details>
    </div>
    """
    return html