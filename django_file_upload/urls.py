# -*- coding: utf-8 -*-

from django.conf.urls import url
from django_file_upload import views as file_views


urlpatterns = [
    url(r'^upload$', file_views.file_upload, name='file_upload'),
]
