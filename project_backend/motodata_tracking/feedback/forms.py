from django import forms
from .models import Feedback

class FeedbackForms(forms.models):

    class Meta:
        model = Feedback
        fields = ["comment"]