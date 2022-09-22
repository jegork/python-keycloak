# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="async-keycloak",
    version="0.28.6",
    url="https://github.com/jegork/python-keycloak",
    license="The MIT License",
    author="Jegor Kitskerkin",
    author_email="jegor.kitskerkin@gmail.com",
    keywords="keycloak openid async httpx",
    description="async-keycloak is a fork of python-keycloak with asyncio support using httpx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["keycloak", "keycloak.authorization", "keycloak.tests"],
    install_requires=["httpx>=0.22.0", "python-jose>=1.4.0"],
    tests_require=["httmock>=1.2.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
    ],
)
