"""
Models for django-nadb
"""
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from managers import PostManager
from markdown import markdown
from django_markup.markup import formatter
import datetime
import settings

class Category(models.Model):
    """
    Category model for Posts
    """
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.TextField(_('description'), blank=True)
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        
    def __unicode__(self):
        return u'%s' % self.name
            
    @permalink
    def get_absolute_url(self):
        return ('category_detail', None, {
            'slug': self.slug
        })

class Post(models.Model):
    """
    Post model
    """
    STATUS_CHOICES = (
        ('d', _('Draft')),
        ('p', _('Published')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='published')
    teaser = models.TextField(_('teaser'))
    body = models.TextField(_('body'))
    body_html = models.TextField(_('body_html'), editable=False, blank=True, null=True)
    status = models.CharField(_('status'),max_length=1, choices=STATUS_CHOICES, default='d')
    author = models.ForeignKey(User, blank=True, null=True)
    published = models.DateTimeField(_('published'), default=datetime.datetime.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    objects = PostManager()
    
    class Meta:
        ordering  = ('-published',)
    
    def __unicode__(self):
        return u'%s' % self.title
        
    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, {
            'year': self.published.year,
            'month': self.published.strftime('%b').lower(),
            'day': self.published.day,
            'slug': self.slug
        })
        
    def save(self):
        """
        Apply a markup format to body and store the output in body_html.
        Customize the markup filter settings in your settings.py
        
        NADB_MARKUP_FILTER = 'codehilite'
        
        MARKUP_SETTINGS = {
            'markdown': {
                'safe_mode': True,
                'extensions': ['codehilite']
            }
        }
                
        """
        filter_name = getattr(settings, 'NADB_MARKUP_FILTER', 'markdown')
        self.body_html = formatter(self.body, filter_name=filter_name)
        super(Post, self).save()
        
