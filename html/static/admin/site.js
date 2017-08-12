document.addEventListener('DOMContentLoaded', function(){
    initCodeMirror();
});


function initCodeMirror() {
    var ta = document.querySelector(".app-blog.change-form textarea[name=content]");
    if (ta == undefined) {
        return;
    }
    CodeMirror.fromTextArea(ta, {mode: "markdown", 
                                 lineWrapping: true, 
                                 theme: "mdn-like",
                                 lineNumbers: false});
}
