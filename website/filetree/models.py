# filetree/models.py
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.files.storage import default_storage

class FileTreeItem(MPTTModel):
    name = models.CharField(max_length=255)
    is_folder = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/', storage=default_storage, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name