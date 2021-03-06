# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-signals-wtf',
    version='0.0.0',
    description='Deal with signals',
    long_description='Same as description',
    author='Florent Messa',
    author_email='florent.messa@gmail.com',
    url='http://github.com/thoas/django-signals-wtf',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
