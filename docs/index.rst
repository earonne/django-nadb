Welcome to nadb's documentation!
================================

nadb (Not Another Django Blog) is a Django blog app. The source repository can be found at https://github.com/earonne/nadb/

Installation
============

Installing nadb is as simple as checking out the source and adding it to your project or ``PYTHONPATH``.

Use git, pip or easy_install to check out nadb from Github_ or get a release from PyPI_.


1. Download and install the package from the python package 
index (PyPI_)::

    easy_install nadb

or if you prefer pip::

    pip install nadb


2. Install the latest development version from GitHub_. This requires to install
git_ of course::

    git clone git://github.com/earonne/nadb.git

then install it manually::

    cd nadb
    python setup.py install


Please note that the dev version is not fully tested and may contain bugs. 

.. _PyPI: http://pypi.python.org/
.. _GitHub: http://www.github.com/
.. _git: http://git-scm.com/


Usage
=============

1. To install ``nadb`` just add the package to your ``INSTALLED_APPS``
setting::

    # settings.py
    INSTALLED_APPS = (
        ...
        'nadb',
        'django-markup',
    )
    
    # Notice you also need to add django-markup to your INSTALLED_APPS.


2. Run the syncdb 
command::  

    $ ./manage.py syncdb


3. Add a line like this in your root URLConf to set up the default URLs for 
nadb::

    # urls.py
    urlpatterns = patterns('',
        url(r'^blog/', include('nadb.urls')),
    )


4. ``nadb`` supports markup filters (e.g. Markdown, RestructuredText, etc.). 
Add the following to your ``settings.py``::

    # settings.py
    NADB_MARKUP_FILTER = 'markdown'
    
    MARKUP_SETTINGS = {
        'markdown': {
            'safe_mode': True,
            'extensions': ['codehilite']
        }
    }


5. Create a ``nadb`` directory inside your templates directory and add 
the following templates::

    base_nadb.html
    post_list.html
    post_detail.html
    post_archive_year.html
    post_archive_month.html
    post_archive_day.html
    category_list.html
    category_detail.html




