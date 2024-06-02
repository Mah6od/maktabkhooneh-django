from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)
    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)
    post = get_object_or_404(posts, pk=pid)

    post.counted_views += 1
    post.save()
    
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

#def test(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'test.html', context)