# django-file-upload
Django File Upload

## Installation
```shell
pip install django-file-upload
```

## Urls.py
```python
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^f/', include('django_file_upload.urls', namespace='django_file_upload')),
]
```
or
```python
from django.urls import re_path
from django_file_upload import views as file_views

urlpatterns = [
    re_path(r'^upload$', file_views.file_upload, name='file_upload'),
]
```

## Settings.py
```python
INSTALLED_APPS = (
    ...
    'django_file_upload',
    ...
)
```
