# filetree/storage.py
from django.core.files.storage import FileSystemStorage
from django.apps import apps
from .utils import create_file_tree_item

class AutoCreateFileTreeStorage(FileSystemStorage):
    def _save(self, name, content):
        name = super()._save(name, content)
        self.create_file_tree_item(name)
        return name

    def create_file_tree_item(self, file_path):
        FileTreeItem = apps.get_model('filetree', 'FileTreeItem')
        create_file_tree_item(file_path, FileTreeItem)