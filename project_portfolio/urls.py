from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('portfolio-details', views.portfolio_details, name="portfolio_details"),
    path('blog-single', views.blog_single, name="blog_single"),
]
