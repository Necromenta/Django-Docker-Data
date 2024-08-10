# filetree/management/commands/scan_uploads.py
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from filetree.models import FileTreeItem

class Command(BaseCommand):
    help = 'Scans the uploads directory and creates FileTreeItem objects'

    def handle(self, *args, **options):
        uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        self.scan_directory(uploads_dir)

    def scan_directory(self, directory, parent=None):
        for item in os.scandir(directory):
            relative_path = os.path.relpath(item.path, settings.MEDIA_ROOT)
            if item.is_file():
                FileTreeItem.objects.get_or_create(
                    name=item.name,
                    is_folder=False,
                    file=relative_path,
                    parent=parent
                )
            elif item.is_dir():
                folder, created = FileTreeItem.objects.get_or_create(
                    name=item.name,
                    is_folder=True,
                    parent=parent
                )
                self.scan_directory(item.path, folder)

        self.stdout.write(self.style.SUCCESS('Successfully scanned uploads directory'))