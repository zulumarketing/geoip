#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

TOP = os.path.dirname(os.path.abspath(__file__))

def list_deps(top):
    with open(os.path.join(top, "requirements.txt")) as fd:
        return [line for line in fd.read().splitlines(False)
                if line.strip() or not line[0] == "#"]

setup(name="geoip-service",
      version="1.5",
      author="Carlos Killpack",
      author_email="carlos@infinite.ai",
      py_modules=["geoip"],
      install_requires=list_deps(TOP))
