from ..componentregistry import ComponentRegistry

@ComponentRegistry.register("Table")
def Table(content, session, headers, pageObj):
    data = content.get("data", [])
    if not data:
        return ""

    title = content.get("title", "")
    merge_info = content.get("mergeInfo", {})
    col_widths = content.get("columnWidths", [])
    
    html_parts = ['<div class="widget table-widget" style="margin: 20px 0; overflow-x: auto;">']
    
    if title:
        alignment = content.get("titleAlignment", "align-center").replace("align-", "text-")
        html_parts.append(f'<div class="widget-header" style="{alignment}; font-weight: bold; margin-bottom: 10px;">{title}</div>')
        
    html_parts.append('<table style="width: 100%; border-collapse: collapse;">')
    
    # 1. Apply column widths if provided
    if col_widths:
        html_parts.append('<colgroup>')
        for width in col_widths:
            html_parts.append(f'<col style="width: {width}px;">')
        html_parts.append('</colgroup>')
        
    # 2. Build the table body
    html_parts.append('<tbody>')
    
    skip_cells = set()
    
    for r, row in enumerate(data):
        html_parts.append('<tr>')
        for c, cell_html in enumerate(row):
            # If this cell is absorbed by a previous row/colspan, skip it
            if (r, c) in skip_cells:
                continue
                
            rowspan = 1
            colspan = 1
            merge_key = f"{r}-{c}"
            
            # Check if this cell spans across multiple rows or columns
            if merge_key in merge_info:
                spans = merge_info[merge_key].split("-") # Format is "rowSpan-colSpan"
                if len(spans) == 2:
                    rowspan = int(spans)
                    colspan = int(spans)
                    
                    # Mark the absorbed cells so we don't render them in future iterations
                    for i in range(r, r + rowspan):
                        for j in range(c, c + colspan):
                            if i == r and j == c:
                                continue # Don't skip the origin cell
                            skip_cells.add((i, j))
                            
            # Use <th> for the first row to make it a header, <td> otherwise
            tag = "th" if r == 0 else "td"
            
            # Build attributes
            attrs = []
            if rowspan > 1: attrs.append(f'rowspan="{rowspan}"')
            if colspan > 1: attrs.append(f'colspan="{colspan}"')
            attr_str = " " + " ".join(attrs) if attrs else ""
            
            # The cell_html usually contains Educative's Quill.js tags (like <p class="ql-align-center">)
            html_parts.append(f'<{tag}{attr_str}>{cell_html}</{tag}>')
            
        html_parts.append('</tr>')
        
    html_parts.append('</tbody></table></div>')
    
    return "".join(html_parts)