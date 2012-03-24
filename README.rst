nadb (Not Another Django Blog app)
==============

A Django blog app.

Installation
------------

From PyPI::

    $ pip install nadb

Or by downloading the source and running::

    $ python setup.py install

Or, for the latest git version::

    $ pip install git+git://github.com/earonne/nadb.git

.. _PyPI: http://pypi.python.org/

Usage
-----

Add ``'nadb'`` to your ``INSTALLED_APPS`` list.

Run the syncdb command::

    $ ./manage.py syncdb

Create your templates::

- base_nadb.html
- post_list.html
- post_detail.html
- post_archive_year.html
- post_archive_month.html
- post_archive_day.html
- category_list.html
- category_detail.html


