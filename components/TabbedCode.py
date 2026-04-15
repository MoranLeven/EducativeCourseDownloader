from ..componentregistry import ComponentRegistry
import html
import uuid

@ComponentRegistry.register("TabbedCode")
def TabbedCode(content, session, headers, pageObj):
    code_contents = content.get("codeContents", [])
    
    if not code_contents:
        return ""
        
    widget_id = f"tc_{uuid.uuid4().hex[:8]}"
    
    html_parts = [f'<div class="widget tabbed-code-widget" id="{widget_id}">']
    
    # 1. Build Tab Navigation Header
    html_parts.append('<div class="tab-header">')
    for i, tab in enumerate(code_contents):
        title = tab.get("title", f"Tab {i+1}")
        tab_id = f"pane_{widget_id}_{i}"
        active_cls = "active" if i == 0 else ""
        html_parts.append(
            f'<button class="tab-btn {active_cls}" onclick="switchTab(\'{widget_id}\', \'{tab_id}\', this)">{title}</button>'
        )
    html_parts.append('</div>')
    
    # 2. Build Tab Content Panes
    html_parts.append('<div class="tab-body">')
    for i, tab in enumerate(code_contents):
        tab_id = f"pane_{widget_id}_{i}"
        display_style = "block" if i == 0 else "none"
        
        # Map Educative language names to Prism.js standard classes
        raw_lang = tab.get("language", "plaintext").lower()
        lang_map = {
            "python310": "python", "c++17": "cpp", "c++": "cpp", 
            "c#": "csharp", "c#12": "csharp", "java-21": "java"
        }
        lang = lang_map.get(raw_lang, raw_lang)
        
        html_parts.append(f'<div class="tab-pane" id="{tab_id}" style="display: {display_style};">')
        
        # Render Main File Content
        main_content = tab.get("content", "")
        main_file = tab.get("entryFileName", "")
        if main_content:
            if main_file:
                html_parts.append(f'<div class="file-name-header">{main_file}</div>')
            safe_main = html.escape(main_content)
            html_parts.append(f'<pre><code class="language-{lang}">{safe_main}</code></pre>')
            
        # Render Additional Attached Files
        additional_files = tab.get("additionalContent", [])
        for add_file in additional_files:
            file_name = add_file.get("fileName", "Additional File")
            file_content = add_file.get("content", "")
            if file_content:
                safe_add = html.escape(file_content)
                html_parts.append(f'<div class="file-name-header" style="margin-top: 20px;">{file_name}</div>')
                html_parts.append(f'<pre><code class="language-{lang}">{safe_add}</code></pre>')
                
        html_parts.append('</div>') # End individual tab pane
        
    html_parts.append('</div></div>') # End tab-body and widget container
    return "".join(html_parts)