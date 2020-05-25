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

Finding the name of the program from which a Python module is running can be trickier than it would seem at first

supports python 3.8 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_cast>`_, mypy static type checking, tested under `Linux, OsX, Windows and Wine <https://travis-ci.org/bitranox/lib_cast>`_, automatic daily builds  and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
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

From source code:

.. code-block:: bash

    # normal install
    python3 setup.py install
    # test without installing
    python3 setup.py test

via pip latest Release:

.. code-block:: bash

    # latest Release from pypi
    python3 -m pip install --upgrade lib_cast

    # test without installing
    python3 -m pip install lib_cast --install-option test

via pip latest Development Version:

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_cast.git --upgrade-strategy eager
    # normal install
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_cast.git
    # test without installing
    python3 -m pip install git+https://github.com/bitranox/lib_cast.git --install-option test

via requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release:
    lib_cast
    # for the latest Development Version :
    lib_cast @ git+https://github.com/bitranox/lib_cast.git


    # to install and upgrade all modules mentioned in requirements.txt:
    python3 -m pip install --upgrade -r /<path>/requirements.txt

via python:

.. code-block:: python

    # for the latest Release
    python3 -m pip install --upgrade lib_cast

    # for the latest Development Version
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_cast.git

Usage
-----------

TBA

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    lib_csv @ git+https://github.com/bitranox/lib_csv.git
    lib_list @ git+https://github.com/bitranox/lib_list.git
    lib_regexp @ git+https://github.com/bitranox/lib_regexp.git

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"
- more test

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

