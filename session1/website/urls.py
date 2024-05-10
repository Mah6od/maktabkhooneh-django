from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    # urls , view, name
    path('', index_view, name= 'index'),
    path('contact', contact_view, name= 'contact'),
    path('about', about_view, name= 'about'),
]