# website/urls.py
from django.urls import path
from . import views

app_name = 'filetree'

urlpatterns = [
    path('', views.file_tree_view, name='file_tree'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]