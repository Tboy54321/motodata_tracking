from django.shortcuts import render, redirect
# from .models import CustomerProfile
# from .forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomerProfileSignUpForm, CustomerProfileUpdateForm
from .models import CustomerProfile

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'username or password is incorrect')

    context = {'page': page}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'User successfully logged out')
    return redirect('login')

def signUpUser(request):
    page = 'signup'

    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = CustomerProfileSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
            
        else:
            messages.success(request, 'An error has occurred during regisration')
    else:
        form = CustomerProfileSignUpForm()
    
    context = {'form': form, 'page': page}
    return render(request, 'login.html', context=context)
            

    # context = {'page': page, 'form': form}
    # return render(request, 'login.html', context)


@login_required(login_url='login')
def usersProfile(request):
    customer_profile, created = CustomerProfile.objects.get_or_create(user=request.user)
    profile = request.user.customerprofile
    edit_form = CustomerProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        edit_form = CustomerProfileUpdateForm(request.POST, instance=profile, user=request.user)

        if edit_form.is_valid():
            edit_form.save(user=request.user)

            return redirect('profile')
        else:
            messages.error(request, 'An error occured during 0registration')
    else:
        edit_form = CustomerProfileUpdateForm(instance=profile, user=request.user)
        
    context = {'customer_profile': customer_profile, 'edit_form': edit_form}
    return render(request, 'users-profile.html', context)

def saProfile(request):
    return render(request, 'sa-profile.html')