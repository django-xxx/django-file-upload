# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.1.6'


setup(
    name='django-file-upload',
    version=version,
    keywords='Django File Upload',
    description='Django File Upload',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/django-xxx/django-file-upload',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_file_upload'],
    py_modules=[],
    install_requires=['TimeConvert', 'django-file-md5>=1.0.2', 'django-logit>=1.1.2', 'django_query', 'django-response', 'django-six'],

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
