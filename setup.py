# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.1'


setup(
    name='django-file-upload',
    version=version,
    keywords='Django File Upload',
    description='Django File Upload',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-file-upload',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_file_upload'],
    py_modules=[],
    install_requires=['django-file-md5>=1.0.2', 'django_logit>=1.1.2', 'django-response'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
