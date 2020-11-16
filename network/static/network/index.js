document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = edit;
    });
});

function edit() {   
    let textarea = document.createElement('textarea');

    let post_div = this.parentElement;
    let original_content_div = post_div.querySelector('.content');  

    textarea.innerHTML = original_content_div.innerHTML;
    
    original_content_div.replaceWith(textarea);
}