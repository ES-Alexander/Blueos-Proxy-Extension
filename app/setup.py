#!/usr/bin/env python3

import os
import ssl

from setuptools import setup

# Ignore ssl if it fails
if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(ssl, "_create_unverified_context", None):
    ssl._create_default_https_context = ssl._create_unverified_context

setup(
    name="example4",
    version="0.1.0",
    description="BlueOS Example Extension 4",
    license="MIT",
    install_requires=[
        "appdirs == 1.4.4",
        "fastapi == 0.109.0",
        "fastapi-versioning == 0.10.0",
        "loguru == 0.5.3",
        "uvicorn == 0.25.0",
        "starlette==0.35.1",
        "aiofiles==0.8.0",
    ],
)