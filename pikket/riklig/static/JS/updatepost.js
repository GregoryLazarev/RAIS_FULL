'use strict'
    
$(document).ready(function(){
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
    $.ajax({
        method: "GET",
        url: "/get_post/"+window.location.pathname.split("/").pop(),
        dataType: "json",
        success: function(data){
            let title = document.querySelector('input[name=title]');
            let content = JSON.parse(data.content);
            title.value = data.title;
            quill.setContents(content["ops"]);
        }
    });


    $('#quill_form').submit(function() {
        let delta = quill.getContents();
        let content = document.querySelector('input[name=content]');
        content.value = JSON.stringify(delta);
    });
});