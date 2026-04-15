from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("LazyLoadPlaceholder")
def LazyLoadPlaceholder(content, session, headers, pageObj):
    message = content.get("message", "Interactive component disabled for offline viewing.")
    
    return f"""
    <div class="widget fallback-widget" style="background-color: #fff3cd; border-color: #ffeeba; color: #856404; padding: 20px; text-align: center; border-radius: 5px; margin: 15px 0;">
        <p>⚠️ <strong>{message}</strong></p>
    </div>
    """