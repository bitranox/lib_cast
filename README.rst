lib_cast
========

|Pypi Status| |license| |maintenance|

|Build Status| |Codecov Status| |Better Code| |code climate| |code climate coverage| |snyk security|

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License
.. |maintenance| image:: https://img.shields.io/maintenance/yes/2021.svg
.. |Build Status| image:: https://travis-ci.org/bitranox/lib_cast.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_cast
.. for the pypi status link note the dashes, not the underscore !
.. |Pypi Status| image:: https://badge.fury.io/py/lib-cast.svg
   :target: https://badge.fury.io/py/lib_cast
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_cast/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_cast
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_cast?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_cast
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_cast/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_cast
.. |code climate| image:: https://api.codeclimate.com/v1/badges/7fa21a0ced3820c5faa9/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_cast/maintainability
   :alt: Maintainability
.. |code climate coverage| image:: https://api.codeclimate.com/v1/badges/7fa21a0ced3820c5faa9/test_coverage
   :target: https://codeclimate.com/github/bitranox/lib_cast/test_coverage
   :alt: Code Coverage

cast float, int, time, file sizes etc. to human readable text with SI Prefixes

it can also be used on the commandline for windows and linux bash



.. code-block:: python

    >>> # cast floating point values
    >>> cast_float_to_human_readable_size(1000,'Volt')
    '1.00 KiloVolt (x10^3)'
    >>> cast_float_to_human_readable_size(0.1,'Volt')
    '100.00 MilliVolt (x10^-3)'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True)
    '100.00 mV (x10^-3)'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True, show_exponent=False)
    '100.00 mV'
    >>> cast_float_to_human_readable_size(0.1,'V', short_form=True, show_exponent=False, remove_trailing_zeros=True)
    '100 mV'

    >>> # cast byte or bit sizes
    >>> cast_float_to_human_readable_size(65535,base1024=True)
    '64 KibiByte (x1024^1)'

    >>> # cast time german
    >>> cast_float_2_human_readable_timediff(2455.456898418)
    '40 Minuten, 55 Sekunden'

    >>> # cast time english
    >>> cast_float_2_human_readable_timediff(2455.456898418, language='en')
    '40 minutes, 55 seconds'

    >>> # cast looong time german
    >>> cast_float_2_human_readable_timediff(89452.456898418)
    '  1 Tage,  0 Stunden, 50 Minuten, 52 Sekunden'

    >>> # AND MANY MORE ! - see usage !

.. code-block::

    IEC Prefixe (2**n)                  ISO Prefixe (10**-n)                ISO Prefixe (10**n)
    =======================             =======================             =======================
    'Ki', 'Kibi', (x1024^1)             'm', 'Milli', (x10^-3)              'k', 'Kilo' , (x10^3)
    'Mi', 'Mebi', (x1024^2)             'µ', 'Mikro', (x10^-6)              'M', 'Mega' , (x10^6)
    'Gi', 'Gibi', (x1024^3)             'n', 'Nano' , (x10^-9)              'G', 'Giga' , (x10^9)
    'Ti', 'Tebi', (x1024^4)             'p', 'Piko' , (x10^-12)             'T', 'Tera' , (x10^12)
    'Pi', 'Pebi', (x1024^5)             'f', 'Femto', (x10^-15)             'P', 'Peta' , (x10^15)
    'Ei', 'Exbi', (x1024^6)             'a', 'Atto' , (x10^-18)             'E', 'Exa'  , (x10^18)
    'Zi', 'Zebi', (x1024^7)             'z', 'Zepto', (x10^-21)             'Z', 'Zetta', (x10^21)
    'Yi', 'Yobi', (x1024^8)             'y', 'Yokto', (x10^-24)             'Y', 'Yotta', (x10^24)

automated tests, Travis Matrix, Documentation, Badges for this Project are managed with `lib_travis_template <https://github
.com/bitranox/lib_travis_template>`_ - check it out

supports python 3.6-3.8, pypy3 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_cast>`_, mypy static type checking, tested under `Linux, macOS, Windows and Wine <https://travis-ci
.org/bitranox/lib_cast>`_, automatic daily builds  and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_cast/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_cast/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_cast/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Installation and Upgrade
------------------------

Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python3 -m pip --upgrade pip
    python3 -m pip --upgrade setuptools
    python3 -m pip --upgrade wheel


install latest version with pip (recommended):

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_cast.git --upgrade-strategy eager

    # test without installing (can be skipped)
    python3 -m pip install git+https://github.com/bitranox/lib_cast.git --install-option test

    # normal install
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_cast.git


install latest pypi Release (if there is any):

.. code-block:: bash

    # latest Release from pypi
    python3 -m pip install --upgrade lib_cast

    # test without installing (can be skipped)
    python3 -m pip install lib_cast --install-option test

    # normal install
    python3 -m pip install --upgrade lib_cast



include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi (if any):
    lib_cast
    # for the latest Development Version :
    lib_cast @ git+https://github.com/bitranox/lib_cast.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python3 -m pip install --upgrade -r /<path>/requirements.txt


Install from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_cast.git
    $ cd lib_cast

    # test without installing (can be skipped)
    python3 setup.py test

    # normal install
    python3 setup.py install


via makefile:

if You are on linux, makefiles are a very convenient way to install. Here we can do much more, like installing virtual environment, clean caches and so on.
This is still in development and not recommended / working at the moment:

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_cast.git
    $ cd lib_cast

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time

Usage from Commandline
------------------------

.. code-block:: bash

   Usage:
       lib_cast (-h | -v | -i)

   Options:
       -h, --help          show help
       -v, --version       show version
       -i, --info          show Info

   this module exposes no other useful functions to the commandline

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    docopt
    lib_csv @ git+https://github.com/bitranox/lib_csv.git
    lib_list @ git+https://github.com/bitranox/lib_list.git
    lib_regexp @ git+https://github.com/bitranox/lib_regexp.git

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_cast/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

0.1.0
-----
2020-05-24:
 - new build matrix
 - mypy strict type testing
 - fix title in pypi documentation
 - drop python2.7 - python 3.4 support

0.0.3
-----
2019-09-03: update setup.py

0.0.2
-----
2019-09-03: refractor

0.0.1
-----
2019-07-22: Initial public release

