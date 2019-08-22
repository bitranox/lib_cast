"""Setuptools entry point."""
import codecs
import os
import sys
import subprocess


def pre_install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


try:
    from setuptools import setup as pip_setup
except ImportError:
    from distutils.core import pip_setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

description = 'Casting'

dirname = os.path.dirname(__file__)
readme_filename = os.path.join(dirname, 'README.rst')

long_description = description
if os.path.exists(readme_filename):
    try:
        readme_content = codecs.open(readme_filename, encoding='utf-8').read()
        long_description = readme_content
    except Exception:
        pass


def setup():
    print('******************************')
    pre_install('git+https://github.com/bitranox/lib_regexp.git')
    pip_setup(
        name='lib_cast',
        version='0.0.1',
        description=description,
        long_description=long_description,
        long_description_content_type='text/x-rst',
        author='Robert Nowotny',
        author_email='rnowotny1966@gmail.com',
        url='https://github.com/bitranox/lib_cast',
        packages=['lib_cast'],
        install_requires=['pytest', 'typing'],
        classifiers=CLASSIFIERS,
        setup_requires=['pytest-runner'],
        tests_require=['pytest'])


setup()
