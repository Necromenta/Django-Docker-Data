# filetree/views.py
import os
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from .models import FileTreeItem
from .utils import create_file_tree_item, ensure_upload_folder

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        relative_root = os.path.relpath(root, settings.MEDIA_ROOT)
        create_file_tree_item(relative_root, FileTreeItem, is_folder=True)
        for file in files:
            file_path = os.path.join(relative_root, file)
            create_file_tree_item(file_path, FileTreeItem, is_folder=False)

def file_tree_view(request):
    ensure_upload_folder(FileTreeItem)
    uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    scan_directory(uploads_dir)
    root_items = FileTreeItem.objects.filter(parent=None)
    return render(request, 'filetree/file_tree.html', {'items': root_items})

def download_file(request, file_id):
    file_item = FileTreeItem.objects.get(id=file_id)
    return FileResponse(file_item.file, as_attachment=True, filename=file_item.name)