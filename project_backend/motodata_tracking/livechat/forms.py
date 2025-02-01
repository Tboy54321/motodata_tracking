from django import forms
from .models import ChatMessage

class chatForm(forms.ModelForm):

    class Meta:
        model = ChatMessage
        fields = ["content"]