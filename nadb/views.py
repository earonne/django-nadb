"""
Views for django-nadb
"""
from django.views.generic import list_detail, date_based
from django.shortcuts import get_object_or_404
from models import Post, Category

def post_list(request, page=0, paginate_by=20,
              template_name='nadb/post_list.html',
              extra_context=None,
              **kwargs):
    """
    Display a list of blog posts.
    
    **Template:**
    
    nadb/post_list.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
    
        ``object_list``
            The list of post objects.
        
        ``is_paginated``
            A boolean representing whether the results are paginated. 
    
    """  
    return list_detail.object_list(
        request,
        queryset=Post.objects.published(),
        paginate_by=paginate_by,
        page=page,
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )


def post_detail(request, year, month, day, slug,
                template_name='nadb/post_detail.html',
                extra_context=None,
                **kwargs):
    """
    Display a blog post.
    
    **Template:**
    
    nadb/post_detail.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
    
        ``object``
            The Post object.
    
    """    
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        slug=slug,
        date_field='published',
        queryset=Post.objects.published(),
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )
    
def post_archive_year(request, year,
                      make_object_list=False,
                      template_name='nadb/post_archive_year.html',
                      extra_context=None,
                      **kwargs):
    """
    Display a list of all months that have published blog posts in a given year. A list of all these blog posts can be included by making make_object_list=True.
    
    **Template:**
    
    nadb/post_archive_year.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
        
        ``date_list``
            A DateQuerySet object containing all months that have have objects available according to queryset, represented as datetime.datetime objects, in ascending order.
        
        ``year``
            The given year, as a four-character string.
        
        ``object_list``
            If the make_object_list parameter is True, this will be set to a list of objects available for the given year, ordered by the date field.
    
    """    
    return date_based.archive_year(
        request,
        year=year,
        date_field='published',
        queryset=Post.objects.published(),
        template_name=template_name,
        extra_context=extra_context,
        make_object_list=make_object_list,
        **kwargs
    )
    
def post_archive_month(request, year, month,
                       template_name='nadb/post_archive_month.html',
                       extra_context=None,
                       **kwargs):
    """
    Display a list of published blog posts in a given month.
    
    **Template:**
    
    nadb/post_archive_month.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
       
       ``date_list``
           A DateQuerySet object containing all days that have have objects available in the given month, represented as datetime.datetime objects, in ascending order.
       
       ``month``
           A datetime.date object representing the given month.
       
       ``next_month``
           A datetime.date object representing the first day of the next month. If the next month is in the future, this will be None.
       
       ``previous_month``
           A datetime.date object representing the first day of the previous month. Unlike next_month, this will never be None.
       
       ``object_list``
           A list of objects available for the given month. 
       
    """
    return date_based.archive_month(
        request,
        year=year,
        month=month,
        date_field='published',
        queryset=Post.objects.published(),
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )
    
def post_archive_day(request, year, month, day,
                     template_name='nadb/post_archive_day.html',
                     extra_context=None,
                     **kwargs):
    """
    Display a list of published blog posts in a given day.
    
    **Template:**
    
    nadb/post_archive_day.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
        
        ``day``
            A datetime.date object representing the given day.
        
        ``next_day``
            A datetime.date object representing the next day. If the next day is in the future, this will be None.
        
        ``previous_day``
            A datetime.date object representing the previous day. Unlike next_day, this will never be None.
        
        ``object_list``
            A list of objects available for the given day.
        
    """
    return date_based.archive_day(
        request,
        year=year,
        month=month,
        day=day,
        date_field='published',
        queryset=Post.objects.published(),
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )
    
def category_list(request, page=0, paginate_by=20,
                  template_name='nadb/category_list.html',
                  extra_context=None,
                  **kwargs):
    """
    Display a list of available blog post categories.
    
    **Template:**
    
    nadb/category_list.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
    
        ``object_list``
            The list of category objects.
        
        ``is_paginated``
            A boolean representing whether the results are paginated. 
        
    """
    return list_detail.object_list(
        request,
        queryset=Category.objects.all(),
        paginate_by=paginate_by,
        page=page,
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )

def category_detail(request, slug, 
                    page=0, paginate_by=20,
                    template_name='nadb/category_detail.html',
                    extra_context=None,
                    **kwargs):
    """
    Display a list of published blog posts in a given category.
    
    **Template:**
    
    nadb/category_detail.html or ``template_name`` keyword argument.
    
    **Template context:**
    
    In addition to extra_context, the template's context will be:
    
        ``object_list``
            The list of post objects.
        
        ``is_paginated``
            A boolean representing whether the results are paginated. 
        
    """
    category = get_object_or_404(Category, slug=slug)
    
    return list_detail.object_list(
        request,
        queryset=category.post_set.published(),
        paginate_by=paginate_by,
        page=page,
        template_name=template_name,
        extra_context={'category': category},
        **kwargs
    )
