# -*- coding: utf-8 -*-
# Copyright © 2015 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
'''Setup for Retweet'''

from setuptools import setup
import os.path

CLASSIFIERS = [
    'Intended Audience :: End Users/Desktop',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7'
]

setup(
    name='retweet',
    version='0.1',
    license='GNU GPL v3',
    description='twitter bot to retweet all tweets from a user',
    long_description='twitter bot to retweet all tweets from a user',
    classifiers=CLASSIFIERS,
    author='Carl Chenet',
    author_email='chaica@ohmytux.com',
    url='https://github.com/chaica/retweet',
    download_url='https://github.com/chaica/retweet',
    packages=['retweet'],
    #data_files=[(os.path.join('share', 'man', 'man1'), ['man/retweet.1'])],
    scripts=['scripts/retweet'],
    install_requires=['tweepy>=3.3.0'],
)
