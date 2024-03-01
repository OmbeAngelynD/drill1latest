

# Create your views here.
from django.shortcuts import render
from .models import Post

def post_detail(request):
    # Assuming you have a URL pattern that captures the post ID
    return render(request, 'home.html')
