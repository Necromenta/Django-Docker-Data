# filetree/utils.py
import os
from django.db import transaction

def create_file_tree_item(path, FileTreeItem, is_folder=False):
    path_parts = path.split(os.path.sep)
    parent = None
    
    with transaction.atomic():
        for i, part in enumerate(path_parts):
            is_last = (i == len(path_parts) - 1)
            item, created = FileTreeItem.objects.get_or_create(
                name=part,
                is_folder=(not is_last) or (is_last and is_folder),
                parent=parent,
                defaults={'file': path if is_last and not is_folder else None}
            )
            parent = item
    
    return item

def ensure_upload_folder(FileTreeItem):
    FileTreeItem.objects.get_or_create(
        name='uploads',
        is_folder=True,
        parent=None
    )