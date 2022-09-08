from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post, Profile


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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already in use')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already in use')
            return redirect('register')
        else:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect(profile)

    else:
        return render(request, 'register.html')
    

def login(request):
    """
    temp docstring
    """
    return render(request, 'login.html')


def profile(request):
    """
    temp docstring
    """
    return render(request, 'index.html')
