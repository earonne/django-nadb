"""
URL patterns for django-nadb.

Simply use a line like this in your root URLConf to set up the default
URLs for django-nadb:

    (r'^blog/', include('nadb.urls')),

Including these URLs (via the ``include()`` directive) will set up the
following patterns based on whatever URL prefix they are included
under:

* Posts list at ``/``.

* Post detail at ``/<year>/<month>/<day>/<slug>``.

* Archive for a day at ``/<year>/<month>/<day>``.

* Archive for a month at ``/<year>/<month>``.

* Archive for a year at ``/<year>``.

* Categories list at ``/categories``.

* Category detail at ``/categories/<slug>``.

"""
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('nadb.views',
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 
                           view='post_detail', 
                           name='post_detail'
                       ),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$', 
                           view='post_archive_day', 
                           name='post_archive_day'
                       ),
                       url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 
                           view='post_archive_month', 
                           name='post_archive_month'
                       ),
                       url(r'^(?P<year>\d{4})/$', 
                           view='post_archive_year', 
                           name='post_archive_year'
                       ),
                       url(r'^categories/(?P<slug>[-\w]+)/$', 
                           view='category_detail', 
                           name='category_detail'
                       ),
                       url(r'^categories/$', 
                           view='category_list', 
                           name='category_list'
                       ),
                       url(r'^$', 
                           view='post_list', 
                           name='post_list'
                       ),
)
