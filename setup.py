#!/usr/bin/env python

###
# python ./setup.py sdist
# twine upload dist/*
###

from distutils.core import setup
import os
import shutil


with open('README.md') as file:
    long_description = file.read()

if not os.path.exists('tmp'):
    os.makedirs('tmp')

if os.path.exists('pbt.py'):
    shutil.copyfile('pbt.py', 'tmp/pbt')

setup(
    name='pbt',
    version='1.0.7',
    description='Prompt decoration for ZSH and Bash written in Python',
    author='Jiri Tyr',
    author_email='jiri.tyr@gmail.com',
    url='http://github.com/jtyr/pbt',
    license='MIT',
    keywords='shell bash zsh bullet train prompt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
    ],
    long_description=long_description,
    packages=['pbt', 'pbt/core', 'pbt/cars'],
    scripts=['tmp/pbt'],
    data_files=[
        ('share/pbt/sources', [
            'sources/ExecTime.bash',
            'sources/ExecTime.zsh']),
        ('share/pbt/themes', [
            'themes/square_brackets_multiline']),
        ('share/doc/pbt', ['LICENSE', 'README.md']),
    ],
)
