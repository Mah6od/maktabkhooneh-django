from django.urls import path
from website.views import *

urlpatterns = [
    # urls , view, name
    path('home', index_view),
    path('contact', contact_view),
    path('about', about_view),

]
