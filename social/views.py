from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Post, Profile


class Posts(generic.ListView):
    """
    temp docstring
    """
    model = Post
    pagination = 12
    template_name = 'index.html'  # temporary template
    queryset = Post.objects.filter(status=1).order_by('-created_on')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


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
            auth.login(request, user_login)

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model,
                                                 id_user=user_model.id)
            new_profile.save()
            return redirect('settings')
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
            messages.success(request, 'You have sucessfully logged in')
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is incorrect')
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


@login_required(login_url='login')
def profile(request):
    """
    temp docstring
    """
    return render(request, 'profile.html')


@login_required(login_url='login')
def settings(request):
    """
    View for user profile settings
    """
    return render(request, 'settings.html')
    # user_profile = Profile.objects.get(user=request.user)

    # if request.method == 'POST':
        
    #     if request.FILES.get('profile_image') is None:
    #         image = user_profile.profile_image
    #         bio = request.POST['bio']
    #         email = request.POST.get('email')
    #         fullname = request.POST.get('fullname')
    #         address = request.POST.get('address')

    #         user_profile.profile_image = image
    #         user_profile.bio = bio
    #         user_profile.fullname = fullname
    #         user_profile.email = email
    #         user_profile.address = address
    #         user_profile.save()

    #     if request.FILES.get('image') is not None:
    #         image = request.FILES.get('profile_image')
    #         bio = request.POST['bio']
    #         email = request.POST.get('email')
    #         fullname = request.POST.get('fullname', False)
    #         address = request.POST.get('address', False)

    #         user_profile.profile_image = image
    #         user_profile.fullname = fullname
    #         user_profile.email = email
    #         user_profile.bio = bio
    #         user_profile.address = address
    #         user_profile.save()
        
    #     return redirect('settings')
    # return render(request, 'settings.html', {'user_profile': user_profile})


def page_not_found(request):
    """
    View to display 404 page
    """
    return render(request, '404.html')
