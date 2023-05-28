from django.shortcuts import render, get_object_or_404
import datetime

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_single(request):
    return render(request, 'blog-single.html')