# django-file-upload
Django File Upload

## Installation
```shell
pip install django-file-upload
```

## Urls.py
```python
urlpatterns = [
    url(r'^f/', include('django_file_upload.urls', namespace='django_file_upload')),
]
```
or
```python
from django.conf.urls import include, url
from django_file_upload import views as file_views

urlpatterns = [
    url(r'^upload$', file_views.file_upload, name='file_upload'),
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
