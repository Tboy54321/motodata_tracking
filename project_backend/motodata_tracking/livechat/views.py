from django.shortcuts import render
from .models import ChatMessage
from .forms import chatForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def chat_room(request, pk):
    form = chatForm()
    # context = {"room_name": room_name}
    if request.method == "POST":
        form = chatForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = request.user
            message.save()

    context = {'form': form}
    return render(request, 'livechat.html', context)