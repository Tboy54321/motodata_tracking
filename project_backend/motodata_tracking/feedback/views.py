from django.shortcuts import render
from .models import Feedback
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.views import role_required

# Create your views here.

@login_required(login_url='login')
# @role_required('customer')
def feedback(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'feedback.html', context)

@login_required(login_url='login')
# @role_required('customer')
def createFeedback(request):
    if request.method == 'POST':
        # rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # if not rating or int(rating) < 1 or int(rating) > 5:
        #     messages.error(request, 'Invalid rating')
        #     return redirect('feedback')
        
        Feedback.objects.create(
            customer=request.user,
            rating=3,
            comment=comment
        )

        messages.success(request, "Thank you for your feedback!")
        return redirect('feedback')
    
    return render (request, 'feedback.html')