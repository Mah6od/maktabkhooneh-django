"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from website.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap
import debug_toolbar

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}

urlpatterns = [
    path(r'', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # urls , view, name
    path('', include("website.urls")),
    path('blog/', include("blog.urls")),
    path('accounts/', include("accounts.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"),
        path('robots.txt', include('robots.urls')),
        path("__debug__/", include("debug_toolbar.urls")),
        path('summernote/', include('django_summernote.urls')),
        path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
