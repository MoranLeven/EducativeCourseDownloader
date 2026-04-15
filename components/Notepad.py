from ..componentregistry import ComponentRegistry
import uuid

@ComponentRegistry.register("Notepad")
def Notepad(content, session, headers, pageObj):
    title = content.get("title", "Notepad")
    placeholder = content.get("placeholderText", "Type your notes here...")
    
    # Generate a unique ID based on the pageId and the widget title/hash to persist local storage
    note_id = f"note_{pageObj.pageId}_{content.get('hash', uuid.uuid4().hex[:8])}"
    
    html = f"""
    <div class="widget notepad-widget">
        <div class="widget-header">{title} <span style="font-size: 0.8em; color: #666; font-weight: normal;">(Saves locally to browser)</span></div>
        <div class="widget-body">
            <textarea id="{note_id}" class="notepad-textarea" placeholder="{placeholder}" rows="6"></textarea>
            <div class="notepad-controls">
                <span id="status_{note_id}" class="notepad-status"></span>
                <button class="nav-btn notepad-btn" onclick="saveNote('{note_id}')">Save Note</button>
            </div>
        </div>
    </div>
    """
    return html