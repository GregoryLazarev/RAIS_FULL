'use strict'

var quill = new Quill('#editor-container', {
    modules: {
        toolbar: [
        [{ header: [1, 2, false] }],
        ['bold', 'italic', 'underline'],
        ['image', 'code-block']
        ]
    },
    placeholder: 'Введите текст.....',
    theme: 'snow'  // or 'bubble'
});

// var form = document.querySelectorAll('form')[1];
$('#quill_form').submit(function() {
    let delta = quill.getContents();
    let content = document.querySelector('input[name=content]');
    content.value = JSON.stringify(delta);
    // return true;
});