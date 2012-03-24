"""
Models for nadb
"""
from django.db import models
import datetime
from django.db.models import permalink
from django.contrib.auth.models import User
from managers import PostManager
from markdown import markdown

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)

class Category(models.Model):
    """
    Category model for Posts
    """
    name = models.CharField('name', max_length=100)
    slug = models.SlugField('slug', unique=True)
    description = models.TextField('description', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
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
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique_for_date='published')
    teaser = models.TextField('teaser')
    body = models.TextField('body')
    body_html = models.TextField(editable=False, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    author = models.ForeignKey(User, blank=True, null=True)
    published = models.DateTimeField('published', default=datetime.datetime.now)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
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
        self.body_html = markdown(self.body, ['codehilite'])
        super(Post, self).save()