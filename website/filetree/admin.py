from django.contrib import admin

# Register your models here.
# filetree/admin.py
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import FileTreeItem

@admin.register(FileTreeItem)
class FileTreeItemAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'is_folder', 'file')
    list_display_links = ('indented_title',)
    list_filter = ('is_folder',)
    search_fields = ('name',)
    
    def indented_title(self, item):
        return f"{'-' * item.level} {item.name}"
    indented_title.short_description = 'Name'

# You can also add a custom admin site to group your models
class FileTreeAdminSite(admin.AdminSite):
    site_header = 'File Tree Administration'
    site_title = 'File Tree Admin'
    index_title = 'File Tree Management'

filetree_admin_site = FileTreeAdminSite(name='filetree_admin')
filetree_admin_site.register(FileTreeItem, FileTreeItemAdmin)