from django import forms
from django.contrib.auth.models import User
from .models import CustomerProfile

class CustomerProfileSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomerProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def save(self, commit=True):
        customer_profile = super().save(commit=False)

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=self.cleaned_data.get('first_name', ''),
            last_name=self.cleaned_data.get('last_name', ''),
            email=self.cleaned_data.get('email', '')
        )

        customer_profile.user = user

        if commit:
            customer_profile.save()
        return customer_profile
