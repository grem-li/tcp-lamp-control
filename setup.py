#!/usr/bin/env python

from setuptools import setup


setup(
    name='tcp-lamp-control',
    version='0.0.1',
    description="Test project for RGB lamp with tcp-server control",
    long_description="Honestly, is just for fun =)",
    python_requires='>=2.7',
    author='Gremli',
    author_email='ya@gremli.ru',
    url='https://github.com/grem-li/tcp-lamp-control',
    packages=['tcp_lamp'],
    scripts=['bin/tcp_lamp'],
    package_dir={'tcp_lamp': 'tcp_lamp'},
    include_package_data=True,
    install_requires=['tornado'],
    license="MIT",
    zip_safe=False,
    keywords=['tornado', 'lamp', 'tlv'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    test_suite='tests',
)
