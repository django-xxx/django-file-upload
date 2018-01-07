==================
django-file-upload
==================

Django File Upload

Installation
============

::

    pip install django-file-upload


Urls.py
=======

::

    urlpatterns = [
        url(r'^f/', include('django_file_upload.urls', namespace='fileupload')),
    ]


or::

    from django.conf.urls import include, url
    from django_file_upload import views as file_views

    urlpatterns = [
        url(r'^upload$', file_views.file_upload, name='file_upload'),
    ]


Settings.py
===========

::

    INSTALLED_APPS = (
        ...
        'django_file_upload',
        ...
    )

