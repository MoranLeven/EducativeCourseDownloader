CSS_STYLE = """
/* Must be at the top of style.css */
@import url("https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css");
@import url("https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css");



/* GLOBAL RESET */
:root { --primary: #3d5afe; --text: #333; --bg: #fff; --card: #fff; }
body { font-family: -apple-system, system-ui, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; padding: 20px; }
.container { max-width: 900px; margin: 0 auto; background: var(--card); padding: 50px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
div.title { font-size: 2.2em; border-bottom: 2px solid #eee; padding-bottom: 15px; margin-bottom: 30px; }


/* body */
body {
    font-family: -apple-system, system-ui, sans-serif;
    line-height: 1.6;
    word-spacing: 1.6;
    color: var(--text);
    background: var(--bg);
    margin: 0;
    padding: 20px;
    margin: 0 auto;
    /* centers horizontally */
    max-width: 900px;
    /* page width */
    padding: 80px 20px;
    /* breathing space */

    background: var(--bg);
    color: var(--text);

    font-family: "Helvetica Neue", SF Pro Display, Arial, Roboto, system-ui;
}


/* SLIDESHOW CONTAINER */
.slideshow-container { position: relative; max-width: 100%; margin: 40px auto; border: 1px solid #ddd; border-radius: 8px; background: #f9f9f9; overflow: hidden; }
/* CANVAS SLIDE */
.mySlides { 
    display: none; 
    position: relative; /* Context for absolute positioning inside */
    width: 100%; 
    overflow: hidden; 
    background: #fff; 
}
.mySlides.active { display: block; }

/* ABSOLUTE POSITIONED ELEMENTS INSIDE SLIDE */
.slide-element {
    position: absolute;
    transform-origin: top left;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden; /* Prevent spillover */
}

/* Specific adjustments for content types */
.slide-element svg { width: 100%; height: 100%; }
.slide-element img { width: 100%; height: 100%; object-fit: contain; }
.slide-text { font-family: 'Verdana', sans-serif; color: #000; line-height: 1.2; white-space: pre-wrap; text-align: left; }


@keyframes fade { from {opacity: .4} to {opacity: 1} }
.prev, .next { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: white; font-weight: bold; font-size: 18px; transition: 0.3s ease; border-radius: 0 3px 3px 0; user-select: none; background-color: rgba(0,0,0,0.4); }
.next { right: 0; border-radius: 3px 0 0 3px; }
.prev:hover, .next:hover { background-color: rgba(0,0,0,0.8); }
.numbertext { color: #f2f2f2; font-size: 12px; padding: 8px 12px; position: absolute; top: 0; left: 0; background: rgba(0,0,0,0.5); border-bottom-right-radius: 5px; }

/* NAV BUTTONS */
.prev, .next { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #333; font-weight: bold; font-size: 18px; transition: 0.3s; border-radius: 0 3px 3px 0; user-select: none; background-color: rgba(200,200,200,0.3); z-index: 100; }
.next { right: 0; border-radius: 3px 0 0 3px; }
.prev:hover, .next:hover { background-color: rgba(0,0,0,0.8); color: white; }
.numbertext { color: #555; font-size: 12px; padding: 8px 12px; position: absolute; top: 0; left: 0; background: rgba(240,240,240,0.9); z-index: 100; border-bottom-right-radius: 5px; font-weight: bold;}

/* OTHER WIDGETS */
.widget { margin: 30px 0; border: 1px solid #eee; border-radius: 8px; overflow: hidden; }
.widget-header { background: #f0f4f8; padding: 10px 20px; font-weight: bold; border-bottom: 1px solid #eee; }
.widget-body { padding: 20px; }
pre { background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; }

/* WIDGETS */
.widget { margin: 30px 0; border: 1px solid #eee; border-radius: 8px; overflow: hidden; }
.widget-header { background: #f0f4f8; padding: 10px 20px; font-weight: bold; border-bottom: 1px solid #eee; }
.widget-body { padding: 20px; }
pre { background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; }

/* NAV LINKS */
.nav-links { display: flex; justify-content: space-between; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
.nav-btn { text-decoration: none; background: var(--primary); color: #fff; padding: 10px 20px; border-radius: 20px; }

/* Notes */
blackquote {
    border-left: 5px solid #cccbff;
    font-size: 18px;
    padding: 16px 20px;
    border-radius: 4px 8px 8px 4px;
    background-color: #f9fafb
}

/* code */
code {
    color: #c7254e;
    background-color: #f9f2f4;
    border-radius: 4px;
    overflow-wrap: break-word;
    border-radius: 0;
    padding-left: 0;
    padding-right: 0;
    font-weight: 300;
    font-size: 14px;
    font-family: Menlo, Monaco, Consolas, Courier New, monospace;
}

pre>code {
    color: #241e1e !important;
}

/* --- SPOILER COMPONENT --- */
.spoiler-widget details { background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 5px; padding: 15px; }
.spoiler-widget summary { cursor: pointer; font-weight: bold; color: var(--primary); outline: none; list-style: none; user-select: none; }
.spoiler-widget summary::-webkit-details-marker { display: none; }
.spoiler-widget summary::before { content: '👁️ '; }
.spoiler-widget details[open] summary::before { content: '🙈 '; }
.spoiler-content { margin-top: 15px; padding-top: 15px; border-top: 1px dashed #ccc; }

/* --- QUIZ COMPONENT --- */
.quiz-widget .widget-body { padding: 30px; }
.quiz-question { margin-bottom: 40px; padding-bottom: 20px; border-bottom: 2px dashed #eee; }
.quiz-question:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.quiz-options { display: flex; flex-direction: column; gap: 12px; margin: 20px 0; }
.quiz-option-container { border: 2px solid #eee; border-radius: 8px; padding: 12px 15px; transition: all 0.2s ease; }
.quiz-label { display: flex; align-items: flex-start; gap: 15px; cursor: pointer; width: 100%; margin: 0; font-size: 1.05em; }
.quiz-label input { margin-top: 6px; cursor: pointer; transform: scale(1.2); }
.quiz-option-text p { margin: 0; }
.quiz-explanation { margin-top: 15px; padding: 15px; background: #fff; border-left: 4px solid var(--primary); font-size: 0.95em; border-radius: 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
.quiz-submit-btn { border: none; cursor: pointer; display: inline-block; font-size: 1em; }

/* Quiz Validation States */
.quiz-option-container.correct { background-color: #f0fdf4; border-color: #86efac; }
.quiz-option-container.incorrect { background-color: #fef2f2; border-color: #fca5a5; opacity: 0.8; }

/* --- NOTEPAD COMPONENT --- */
.notepad-textarea { width: 100%; padding: 15px; border: 1px solid #ccc; border-radius: 5px; font-family: inherit; font-size: 1em; resize: vertical; box-sizing: border-box; }
.notepad-textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 5px rgba(61, 90, 254, 0.3); }
.notepad-controls { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }
.notepad-btn { cursor: pointer; border: none; font-size: 0.9em; padding: 8px 16px; }
.notepad-status { color: #28a745; font-size: 0.9em; opacity: 0; transition: opacity 0.3s ease; }

/* --- TABLE HTML COMPONENT (Tailwind Fallbacks) --- */
.table-widget table { width: 100%; border-collapse: collapse; margin-bottom: 0; }
.table-widget td, .table-widget th { border: 1px solid #e5e7eb; padding: 12px 15px; text-align: left; }
.table-widget tr:nth-child(even) td { background-color: #fafafa; }
/* Override inline educative styles that might look bad offline */
.table-widget td[style*="background-color:#F5F5F5"] { background-color: #f3f4f6 !important; font-weight: bold; }

/* --- TABBED CODE COMPONENT --- */
.tabbed-code-widget { border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; margin: 20px 0; background: #fff; }
.tabbed-code-widget .tab-header { display: flex; background: #f3f4f6; border-bottom: 1px solid #e5e7eb; overflow-x: auto; }
.tabbed-code-widget .tab-btn { background: transparent; border: none; padding: 12px 20px; cursor: pointer; font-size: 0.9em; font-weight: 500; color: #4b5563; border-bottom: 2px solid transparent; transition: all 0.2s; white-space: nowrap; }
.tabbed-code-widget .tab-btn:hover { color: #111827; background: #e5e7eb; }
.tabbed-code-widget .tab-btn.active { color: var(--primary, #2563eb); border-bottom-color: var(--primary, #2563eb); background: #fff; }
.tabbed-code-widget .tab-body { padding: 15px; }
.tabbed-code-widget .file-name-header { font-family: monospace; font-size: 0.85em; color: #6b7280; margin-bottom: 5px; text-transform: uppercase; font-weight: bold; background: #f9fafb; display: inline-block; padding: 4px 8px; border-radius: 4px; border: 1px solid #e5e7eb; }
.tabbed-code-widget pre { margin-top: 0; border-radius: 6px; }

/* --- QUILL EDITOR FALLBACKS (Used inside Tables) --- */
.ql-align-center { text-align: center; }
.ql-align-right { text-align: right; }
.ql-align-justify { text-align: justify; }
.table-widget th p, .table-widget td p { margin: 0; padding: 4px 0; }
"""



JS_SCRIPT = """
document.addEventListener("DOMContentLoaded", function() {
    let slideshows = document.querySelectorAll(".slideshow-container");
    slideshows.forEach(slideshow => {
        showSlide(slideshow.id, 0);
    });
});

function moveSlide(containerId, n) {
    let container = document.getElementById(containerId);
    let slides = container.getElementsByClassName("mySlides");
    let currentActiveIndex = -1;
    for (let i = 0; i < slides.length; i++) {
        if (slides[i].classList.contains("active")) {
            currentActiveIndex = i;
            break;
        }
    }
    let newIndex = currentActiveIndex + n;
    if (newIndex >= slides.length) { newIndex = 0; }
    if (newIndex < 0) { newIndex = slides.length - 1; }
    showSlide(containerId, newIndex);
}

function showSlide(containerId, index) {
    let container = document.getElementById(containerId);
    let slides = container.getElementsByClassName("mySlides");
    let numberText = container.getElementsByClassName("numbertext")[0];
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
        slides[i].style.display = "none";
    }
    slides[index].classList.add("active");
    slides[index].style.display = "block";
    if (numberText) {
        numberText.innerText = (index + 1) + " / " + slides.length;
    }
}

// --- QUIZ EVALUATION LOGIC ---
function evaluateQuiz(questionId) {
    const questionDiv = document.getElementById(questionId);
    const inputs = questionDiv.querySelectorAll('input');
    
    // Evaluate each option
    inputs.forEach(input => {
        const isCorrect = input.getAttribute('data-correct') === 'true';
        const isChecked = input.checked;
        const container = document.getElementById('container_' + input.value);
        const explanation = document.getElementById('exp_' + input.value);
        
        // Reset classes
        container.classList.remove('correct', 'incorrect');
        explanation.style.display = 'none';

        if (isChecked) {
            // User selected this option
            if (isCorrect) {
                container.classList.add('correct');
            } else {
                container.classList.add('incorrect');
            }
            explanation.style.display = 'block';
        } else if (isCorrect && !isChecked) {
            // User missed a correct option (highlight it to show them what they missed)
            container.classList.add('correct');
            explanation.style.display = 'block';
        }
        
        // Lock the inputs so the user can't change their answer after submitting
        input.disabled = true;
    });
    
    // Hide the submit button after clicking
    const btn = questionDiv.querySelector('.quiz-submit-btn');
    if(btn) btn.style.display = 'none';
}

// --- NOTEPAD LOGIC ---
document.addEventListener("DOMContentLoaded", function() {
    // Load saved notes when the page loads
    let textareas = document.querySelectorAll('.notepad-textarea');
    textareas.forEach(ta => {
        let savedText = localStorage.getItem(ta.id);
        if (savedText) {
            ta.value = savedText;
        }
    });
});

function saveNote(noteId) {
    const textarea = document.getElementById(noteId);
    const statusLabel = document.getElementById('status_' + noteId);
    
    if (textarea) {
        localStorage.setItem(noteId, textarea.value);
        
        // Show saved status
        statusLabel.innerText = "✓ Saved locally";
        statusLabel.style.opacity = 1;
        
        // Fade out status after 2 seconds
        setTimeout(() => {
            statusLabel.style.opacity = 0;
        }, 2000);
    }
}

// --- TABBED CODE LOGIC ---
function switchTab(widgetId, paneId, clickedBtn) {
    // 1. Get the parent widget container
    const widget = document.getElementById(widgetId);
    if (!widget) return;
    
    // 2. Remove 'active' class from all buttons in this specific widget
    const buttons = widget.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // 3. Hide all tab panes in this specific widget
    const panes = widget.querySelectorAll('.tab-pane');
    panes.forEach(pane => pane.style.display = 'none');
    
    // 4. Activate the clicked button and show the targeted pane
    clickedBtn.classList.add('active');
    const activePane = document.getElementById(paneId);
    if (activePane) {
        activePane.style.display = 'block';
    }
}

"""