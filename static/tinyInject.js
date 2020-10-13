var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/e7j70r1z2cushh55bkn9bbfe4sa43n6ufim2jo8u7r95xs7a/tinymce/5/tinymce.min.js"
document.head.appendChild(script)

script.onload = function(){
tinymce.init({
    selector: '#id_content',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
  });
}
