from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Latex")
def Latex(content, session, headers, pageObj):
    text = content.get("text", "")
    
    if not text:
        return ""
        
    # Inject the MathJax script directly into the component's HTML.
    # The 'if (!window.MathJax)' check ensures we don't overwrite the config 
    # if there are multiple Latex components on the same page.
    return f"""
    <div class="widget latex-widget" style="margin: 15px 0;">
        <script>
            if (!window.MathJax) {{
                window.MathJax = {{
                    tex: {{
                        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
                    }}
                }};
            }}
        </script>
        <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        
        <div style="overflow-x: auto; padding: 15px; background: #f8f9fa; border: 1px solid #eee; border-radius: 5px;">
            \\[ {text} \\]
        </div>
    </div>
    """