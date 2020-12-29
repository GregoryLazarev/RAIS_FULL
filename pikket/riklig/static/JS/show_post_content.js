'use strict'
$(document).ready(function(){
    let Delta = Quill.import('delta');    
    $('.card-text').each(function(i, elem) { 
        let d = new Delta(JSON.parse(elem.innerHTML));
        let quill = new Quill(elem);
        quill.setContents(d);
        elem.innerHTML = quill.root.innerHTML;
        elem.classList.remove('ql-container');
    });
});