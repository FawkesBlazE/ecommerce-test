from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def checkout(request):
    if request.method == 'POST':
        print(request.POST)
    context = {}
    template = 'checkout.html'
    return render(request, template, context)
