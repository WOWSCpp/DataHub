from django.urls import path
from .views import * 

urlpatterns = [
    path('home/', home, name='home'),
    path('upload/', jump_to_upload_page, name='upload'),
    path('download/', download, name='download')
]
