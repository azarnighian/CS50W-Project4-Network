document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.edit_button').forEach(function(button) {
        button.onclick = edit;
    });
    document.querySelectorAll('.save_button').forEach(function (button) {
        button.onclick = save_edit;
    });
});

function edit() {   
    let textarea = document.createElement('textarea');

    post_div = this.parentElement;
    let original_content_div = post_div.querySelector('.content');  

    textarea.value = original_content_div.innerHTML;
    
    original_content_div.replaceWith(textarea);

    save_button = post_div.querySelector('.save_button');
    save_button.style.display = "block";
}

function save_edit() {       
    let post_id = post_div.querySelector('.post_id').innerHTML;

    let textarea = document.querySelector(".posts textarea");
    let updated_content = textarea.value;

    // change model content
    fetch(`/save_edit/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            content: updated_content
        })
    })

    // change textarea back to div
    let content_div = document.createElement('div');
    content_div.classList.add("content");
    content_div.innerHTML = updated_content;
    
    textarea.replaceWith(content_div);

    // hide save button
    save_button.style.display = "none";
}