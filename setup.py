# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='sphinxcontrib-merge',
    version='0.1.0',
    url='https://github.com/dgarcia360/sphinxcontrib-merge',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-merge',
    license='MIT',
    author='David Garcia',
    author_email='dgarcia360@outlook.com',
    description='Build Sphinx documentation from multiple remote sources.',
    long_description="",
    zip_safe=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Utilities',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    platforms='any',
    include_package_data=True,
    install_requires=['Sphinx>=1.1', 'requests'],
    packages=find_packages(exclude=['docs']),
    namespace_packages=['sphinxcontrib']
)
