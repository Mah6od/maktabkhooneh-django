from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_view(request, **kwargs): # cat_name=None, author_username=None
    now = timezone.now()
    posts = Post.objects.filter(status = 1,
                                published_date__lte=now) #order_by('published_date')
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])

    if kwargs.get('author_username') != None:
            posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)
    post = get_object_or_404(posts, pk=pid)

    post.counted_views += 1
    post.save()

    # Find the index of the current post
    post_index = list(posts).index(post)

    # Get previous and next posts
    next_post = posts[post_index - 1] if post_index > 0 else None
    prev_post = posts[post_index + 1] if post_index < len(posts) - 1 else None

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-single.html', context)

#def test(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    # print(request.__dict__)
    now = timezone.now()
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
         # print(request.GET.get('s'))
         if s := request.GET.get('s'): # Walrus
            posts = posts.filter(content__contains=s)
         
    
    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)