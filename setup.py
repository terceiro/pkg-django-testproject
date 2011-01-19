#!/usr/bin/env python
# Copyright (C) 2010 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of django-testscenarios.
#
# django-testscenarios is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# django-testscenarios is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with django-testscenarios.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name = 'django-testscenarios',
    version = "0.5.1",
    author = "Zygmunt Krynicki",
    author_email = "zygmunt.krynicki@linaro.org",
    description = "Django-compatible testscenarios.TestWithScenarios",
    url = 'https://launchpad.net/django-testscenarios',
    test_suite = 'test_project.tests.run_tests',
    license='LGPLv3',
    keywords = ['django', 'testing', 'scenarios'],
    classifiers = [
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Testing",
    ],
    zip_safe = True,
    packages = [
        'django_testproject',
        'django_testscenarios',
    ],
    # dependencies
    install_requires=[
        'django >= 1.0',
        'testtools >= 0.9.2',
        'testscenarios >= 0.2',
    ],
)
