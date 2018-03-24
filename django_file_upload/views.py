# -*- coding: utf-8 -*-

from __future__ import division

import os

from django.conf import settings
from django.core.files.storage import default_storage
from django_file_md5 import calculate_md5
from django_logit import logit
from django_response import response


@logit
def file_upload(request):
    # File Not Found
    if not request.FILES:
        return response(settings.FILE_NOT_FOUND if hasattr(settings, 'FILE_NOT_FOUND') else 999999)

    # File Object
    file_ = request.FILES.get('file', '')

    # File Ext
    ext = os.path.splitext(file_.name)[-1]

    # File Path
    file_path = '{0}/{1}{2}'.format('file', calculate_md5(file_), ext)

    # File Save
    if not default_storage.exists(file_path):
        default_storage.save(file_path, file_)

    return response(200, 'File Upload Success', u'文件上传成功', data={
        'file_path': file_path,
        'file_url': '{0}{1}'.format(settings.DOMAIN if hasattr(settings, 'DOMAIN') else '', default_storage.url(file_path)),
    })
