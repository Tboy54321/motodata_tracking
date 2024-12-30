from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from functools import wraps
from .forms import CustomerProfileSignUpForm, CustomerProfileUpdateForm, SAProfileSignUpForm, SAProfileUpdateForm
from .models import CustomerProfile


def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.customerprofile.role == required_role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

# Create your views here.

def loginAccount(request):
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
            if request.user.customerprofile.role == 'customer':
                return redirect('profile')
            elif request.user.customerprofile.role == 'service_adviser':
                return redirect('sa-profile')
        else:
            messages.error(request, 'username or password is incorrect')

    context = {'page': page}
    return render(request, 'login.html', context)

def logoutAccount(request):
    logout(request)
    messages.error(request, 'User successfully logged out')
    return redirect('login')

def deleteAccount(request):
    
    if request.method == 'POST':
        user = request.user

        user.delete()
        messages.success(request, 'Account deleted successfuly')
        return redirect('login')
    
    return render(request, 'delete-account.html')

def signUpUser(request):
    page = 'signupUser'

    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = CustomerProfileSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_profile = user.customerprofile
            customer_profile.role = 'customer'
            customer_profile.save()
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
@role_required('customer')
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
            messages.error(request, 'An error occured during update')
    else:
        edit_form = CustomerProfileUpdateForm(instance=profile, user=request.user)
        
    context = {'customer_profile': customer_profile, 'edit_form': edit_form}
    return render(request, 'users-profile.html', context)

@login_required(login_url='login')
@role_required('customer')
def userEditProfile(request):
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
        
    context = {'edit_form': edit_form}
    return render(request, 'edit-userprofile.html', context)


def signupSA(request):
    page = 'signupSA'

    if request.user.is_authenticated:
        return redirect('sa-profile')
    
    if request.method == 'POST':
        form = SAProfileSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_profile = user.customerprofile
            customer_profile.role = 'service_adviser'
            customer_profile.save()
            login(request, user)
            return redirect('sa-profile')
        else:
            messages.success(request, 'An error has occurred during regisration')
    else:
        form = SAProfileSignUpForm()

    context = {'form': form, 'page': page}
    return render(request, 'login.html', context)

# NOT YET IMPLEMENTED
@login_required(login_url='login')
@role_required('service_adviser')
def saProfile(request):
    sa_profile, created = CustomerProfile.objects.get_or_create(user=request.user)
    profile = request.user.customerprofile
    edit_form = SAProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        edit_form = SAProfileUpdateForm(request.POST, instance=profile, user=request.user)

        if edit_form.is_valid():
            edit_form.save(user=request.user)

            return redirect('sa-profile')
        else:
            messages.error(request, 'An error occured during update')
    else:
        edit_form = SAProfileUpdateForm(instance=profile, user=request.user)

    context = {'sa_profile': sa_profile, 'edit_form': edit_form}
    return render(request, 'sa-profile.html', context)

@login_required(login_url='login')
@role_required('service_adviser')
def saEditProfile(request):
    profile = request.user.customerprofile
    edit_form = SAProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        edit_form = SAProfileUpdateForm(request.POST, instance=profile, user=request.user)

        if edit_form.is_valid():
            edit_form.save(user=request.user)

            return redirect('sa-profile')
        else:
            messages.error(request, 'An error occured during registration')
    else:
        edit_form = SAProfileUpdateForm(instance=profile, user=request.user)
        
    context = {'edit_form': edit_form}
    return render(request, 'edit-saprofile.html', context)

def home(request):
    return render (request, 'home.html')

# UPDATE PASSWORD USING MAIL