# -*- coding: utf-8 -*-

from django_six import re_path

from django_file_upload import views as file_views


app_name = 'django_file_upload'


urlpatterns = [
    re_path(r'^upload$', file_views.file_upload, name='file_upload'),
]
