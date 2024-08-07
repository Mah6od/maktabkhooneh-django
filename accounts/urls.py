from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout/', views.logout_view, name='logout'),
    # registration / signup
    path('signup/', views.signup_view, name='signup'),
    # forgot password
    path('forgot/', auth_views.PasswordResetView.as_view(template_name='accounts/forgot.html'), name='forgot'),
    path('forgot/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
