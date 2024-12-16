from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerProfile
from django.contrib.auth.password_validation import validate_password

class CustomerProfileSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address']

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