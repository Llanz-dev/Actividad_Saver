from django.shortcuts import render
from lists.models import Tasks

# Create your views here.
def home(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'lists/home.html', context)