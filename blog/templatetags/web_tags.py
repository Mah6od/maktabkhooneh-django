from django import template
from blog.models import Post, Category
from django.utils.text import slugify

register = template.Library()

@register.inclusion_tag('website/web-blog-contents.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts':posts}