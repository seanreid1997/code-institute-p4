from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Post, Profile


@login_required(login_url='login')
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
            user = User.objects.create_user(email=email, username=username,
                                            password=password)
            user.save()

            # log user in and redirect to settings page
            user_login = auth.authenticate(username=username, 
                                           password=password)
            auth.login(request, 'settings')

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model,
                                                 id_user=user_model.id)
            new_profile.save()
            return redirect(profile)

    else:
        return render(request, 'register.html')


def login(request):
    """
    temp docstring
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')

    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    """
    Function to sign user out and
    redirect them to login page
    """
    auth.logout(request)
    return redirect('login')


def profile(request):
    """
    temp docstring
    """
    return render(request, 'index.html')


@login_required(login_url='login')
def settings(request):
    """
    View for user profile settings
    """
    return render(request, 'settings.html')
