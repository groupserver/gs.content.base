# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2011, 2012, 2013, 2014, 2016 OnlineGroups.net and 
# Contributors.
#
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

name = 'gs.content.base'
version = get_version()

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"),
                 encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(
    name=name,
    version=version,
    description="Core code for Web pages in GroupServer.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='zope, page, view, site',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://github.com/groupserver/{0}'.format(name),
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['.'.join(name.split('.')[:i])
                        for i in range(1, len(name.split('.')))],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.component',
        'Zope2',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
# --=mpj17=-- These are required, but problematic. If I take them out
# then GroupServer will still build fine (because of buildout.cfg) and
# so will the setup.py on ReadTheDocs. If I leave them in I have to
# start pointing ReadTheDocs at Products.NuxUserFolderWithGroups, which is
# required by the CustomUserFolder, and I do not want that.
#        'Products.GSContent',  # For the site info
#        'Products.CustomUserFolder',  # For the logged in user info
# TODO: Move the logged-in user info to gs.profile.loggedin
# TODO: Move the SiteInfo to gs.site.info
