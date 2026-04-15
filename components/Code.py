from ..componentregistry import ComponentRegistry
import html

@ComponentRegistry.register("Code")
def Code(content, session, headers, pageObj):
    # Extract the raw code text
    code_text = content.get("content", "")
    
    if not code_text:
        return ""
        
    # Extract language for syntax highlighting
    raw_lang = content.get("language", "plaintext").lower()
    
    # Map Educative language names to standard Prism.js classes
    lang_map = {
        "python310": "python", "c++17": "cpp", "c++": "cpp", 
        "c#": "csharp", "c#12": "csharp", "java-21": "java"
    }
    lang = lang_map.get(raw_lang, raw_lang)

    # Figure out the best title/header to display (prioritize caption, then filename)
    file_name = content.get("caption") or content.get("entryFileName") or content.get("title") or ""
    
    # Escape HTML characters so code like <div> or Generics <T> doesn't break the page layout
    safe_code = html.escape(code_text)

    html_parts = ['<div class="widget code-widget" style="margin: 20px 0; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; background: #fff;">']
    
    # Add a file header if we found one, otherwise just show the language name
    header_text = file_name if file_name else lang.upper()
    html_parts.append(f'''
        <div class="code-header" style="background: #f9fafb; padding: 8px 15px; border-bottom: 1px solid #e5e7eb; font-family: monospace; font-size: 0.85em; color: #6b7280; font-weight: bold;">
            {header_text}
        </div>
    ''')
    
    # Add the pre/code block for Prism.js to target
    html_parts.append(f'''
        <div class="widget-body" style="padding: 0;">
            <pre style="margin: 0; padding: 15px; border-radius: 0; background: transparent;"><code class="language-{lang}">{safe_code}</code></pre>
        </div>
    </div>
    ''')

    return "".join(html_parts)