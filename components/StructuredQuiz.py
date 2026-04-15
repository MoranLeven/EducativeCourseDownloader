from ..componentregistry import ComponentRegistry
import uuid

@ComponentRegistry.register("StructuredQuiz")
def StructuredQuiz(content, session, headers, pageObj):
    questions = content.get("questions", [])
    title = content.get("title", "Quiz Assessment")
    
    html_parts = [f'<div class="widget quiz-widget structured-quiz"><div class="widget-header">{title}</div><div class="widget-body">']
    
    for q in questions:
        q_id = q.get("id", f"sq_{uuid.uuid4().hex[:8]}")
        # Structured quizzes sometimes use different keys for the text
        q_text_html = q.get("questionTextHtml", q.get("mdHtml", "Question text missing"))
        is_multiple = q.get("multipleAnswers", False)
        
        # Options can be nested differently depending on the quiz type
        options = q.get("questionOptions", q.get("options", []))
        input_type = "checkbox" if is_multiple else "radio"
        
        html_parts.append(f'<div class="quiz-question" id="{q_id}">')
        html_parts.append(f'<div class="question-text">{q_text_html}</div>')
        html_parts.append('<div class="quiz-options">')
        
        for opt in options:
            opt_id = opt.get("id", f"opt_{uuid.uuid4().hex[:8]}")
            opt_html = opt.get("mdHtml", opt.get("text", ""))
            is_correct = str(opt.get("correct", False)).lower()
            explanation = opt.get("explanation", {}).get("mdHtml", "")
            
            html_parts.append(f'''
                <div class="quiz-option-container" id="container_{opt_id}">
                    <label class="quiz-label">
                        <input type="{input_type}" name="{q_id}" value="{opt_id}" data-correct="{is_correct}">
                        <div class="quiz-option-text">{opt_html}</div>
                    </label>
                    <div class="quiz-explanation" id="exp_{opt_id}" style="display: none;">
                        {explanation if explanation.strip() else '<em>Correct.</em>'}
                    </div>
                </div>
            ''')
        
        html_parts.append('</div>')
        # Reuses the evaluateQuiz JS function from the standard Quiz component
        html_parts.append(f'<button class="quiz-submit-btn nav-btn" onclick="evaluateQuiz(\'{q_id}\')">Submit Answer</button>')
        html_parts.append('</div>')
        
    html_parts.append('</div></div>')
    return "".join(html_parts)