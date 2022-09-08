from django.shortcuts import render
from django.views import generic
from .models import Post


class Posts(generic.ListView):
    """
    temp docstring
    """
    model = Post
    pagination = 12
    template_name = 'index.html'  # temporary template
    queryset = Post.objects.filter(status=1).order_by('-created_on')


def register(request):
    """
    temp docstring
    """
    if request.method == 'POST':
        pass
    else:
        return render(request, 'register.html')
    

def login(request):
    """
    temp docstring
    """
    return render(request, 'login.html')
