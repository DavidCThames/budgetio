from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'budget_calc'
urlpatterns = [
    url(r'^/?$', views.search, name="get_all"),
]