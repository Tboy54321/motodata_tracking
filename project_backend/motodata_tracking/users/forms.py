from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerProfile
from django.contrib.auth.password_validation import validate_password

class CustomerProfileSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'username', 'email', 'phone_number', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
            CustomerProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )
        return user


class CustomerProfileUpdateForm(forms.ModelForm):
    # Include fields from the User model
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = CustomerProfile
        fields = ['phone_number', 'address']  # Fields from CustomerProfile

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
            self.fields['username'].initial = user.username

    def save(self, user=None, commit=True):
        customer_profile = super().save(commit=False)

        # Update User model fields
        if user:
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.save()

        if commit:
            customer_profile.save()

        return customer_profile
