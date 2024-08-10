// filetree/static/filetree/js/filetree.js
document.addEventListener('DOMContentLoaded', function() {
    var fileTree = document.querySelector('.file-tree');

    fileTree.addEventListener('click', function(event) {
        var target = event.target;

        if (target.classList.contains('folder')) {
            var li = target.closest('li');
            li.classList.toggle('expanded');
            var children = li.querySelector('.children');
            if (children) {
                children.style.display = children.style.display === 'none' ? 'block' : 'none';
            }
        } else if (target.classList.contains('file')) {
            var fileId = target.getAttribute('data-id');
            window.location.href = '/filetree/download/' + fileId + '/';
        }
    });
});