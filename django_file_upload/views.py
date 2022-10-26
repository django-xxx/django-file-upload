# -*- coding: utf-8 -*-

from __future__ import division

import os

from django.conf import settings
from django.core.files.storage import default_storage
from django_file_md5 import calculate_md5
from django_logit import logit
from django_query import get_query_value
from django_response import response
from TimeConvert import TimeConvert as tc


@logit
def file_upload(request):
    # File Not Found
    if not request.FILES:
        return response(settings.DJANGO_FILE_UPLOAD_FILE_NOT_FOUND if hasattr(settings, 'DJANGO_FILE_UPLOAD_FILE_NOT_FOUND') else 999999)

    # File Object
    file_ = request.FILES.get('file', '')

    # DC: 0 or 1
    direct_callback = get_query_value(request, 'dc', default=0, val_cast_func=int) or (hasattr(settings, 'DJANGO_FILE_UPLOAD_DIRECT_CALLBACK') and settings.DJANGO_FILE_UPLOAD_DIRECT_CALLBACK)

    file_path, file_url = None, None

    # If Not Direct Callback
    if not direct_callback:
        # File Ext
        ext = os.path.splitext(file_.name)[-1]

        # Joint File Path
        # Base Path
        base_path = settings.DJANGO_FILE_UPLOAD_BASE_PATH if hasattr(settings, 'DJANGO_FILE_UPLOAD_BASE_PATH') else 'file'
        if hasattr(settings, 'DJANGO_FILE_UPLOAD_BASE_PATH_CALLBACK_FUNC') and hasattr(settings.DJANGO_FILE_UPLOAD_BASE_PATH_CALLBACK_FUNC, '__call__'):
            base_path = settings.DJANGO_FILE_UPLOAD_BASE_PATH_CALLBACK_FUNC(request) or 'file'
        # YM Path
        ym_path = tc.local_string(format='%Y%m') if hasattr(settings, 'DJANGO_FILE_UPLOAD_USE_YM') and settings.DJANGO_FILE_UPLOAD_USE_YM else ''
        # File Name
        file_name = tc.local_string(format='%Y%m%d%H%M%S') if hasattr(settings, 'DJANGO_FILE_UPLOAD_USE_DT') and settings.DJANGO_FILE_UPLOAD_USE_DT else calculate_md5(file_)
        # File Path
        file_path = '{0}/{1}{2}{3}{4}'.format(base_path, ym_path, ym_path and '/', file_name, ext)

        # File Save/URL call `DJANGO_FILE_UPLOAD_STORAGE_FUNC`
        storage_resp = {}
        if hasattr(settings, 'DJANGO_FILE_UPLOAD_STORAGE_FUNC') and hasattr(settings.DJANGO_FILE_UPLOAD_STORAGE_FUNC, '__call__'):
            storage_resp = settings.DJANGO_FILE_UPLOAD_STORAGE_FUNC(request, file_path) or {}

        # File Save/URL call `default_storage`
        if not storage_resp.get('file_url'):
            if not default_storage.exists(file_path):
                default_storage.save(file_path, file_)
            file_url = '{0}{1}'.format(settings.DOMAIN if hasattr(settings, 'DOMAIN') else '', default_storage.url(file_path))
            storage_resp['file_url'] = file_url

        if 'file_path' not in storage_resp:
            storage_resp['file_path'] = file_path

    callback_resp = {}
    if hasattr(settings, 'DJANGO_FILE_UPLOAD_CALLBACK_FUNC') and hasattr(settings.DJANGO_FILE_UPLOAD_CALLBACK_FUNC, '__call__'):
        callback_resp = settings.DJANGO_FILE_UPLOAD_CALLBACK_FUNC(request, file_path, file_url) or {}

    return response(200, 'File Upload Success', u'文件上传成功', data=dict(storage_resp, **callback_resp))
