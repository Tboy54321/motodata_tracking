from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def feedback(request):
    return render(request, 'feedback.html')