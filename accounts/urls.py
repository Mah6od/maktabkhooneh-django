from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout/', views.logout_view, name='logout'),
    # registeration / signup
    path('signup/', views.signup_view, name='signup'),
    # forgot
    path('forgot/', views.forgot_view, name='forgot'),
]