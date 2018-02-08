"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # Login page using Django's default login view (not views.login)
    url(r'^login/$', login, {'template_name': 'users/login.html'},
    name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
