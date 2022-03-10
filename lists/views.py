import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from lists.models import Tasks
from lists.forms import TodoForm

# Create your views here.


def home(request):        
    tasks = Tasks.objects.all().order_by('-id')
    completed_count = Tasks.objects.all().filter(completed=True).count
    completed = Tasks.objects.all().filter(completed=True).all().order_by('id')
    
    context = {'tasks': tasks, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/home.html', context)


def search_item(request):
    completed_count = Tasks.objects.all().filter(completed=True).count
    completed = Tasks.objects.all().filter(completed=True).all().order_by('id')    
    searched = request.GET
    search_count = Tasks.objects.filter(title__contains=searched).count 
    tasks = Tasks.objects.all().order_by('-id') 
    has_searched = False

    if 'searched' in request.GET:   
        has_searched = True    
        searched = request.GET['searched']
        tasks = Tasks.objects.filter(title__contains=searched).order_by('-id')
        search_count = Tasks.objects.filter(title__contains=searched).count        
        completed_count = Tasks.objects.filter(title__contains=searched).filter(completed=True).count
        completed = Tasks.objects.filter(title__contains=searched).filter(completed=True).all().order_by('id')                        
    else:
        return redirect('home')

    
    context = {'tasks': tasks, 'completed_count': completed_count, 'completed': completed, 'searched': searched, 'search_count': search_count, 'has_search': has_searched}
    return render(request, 'lists/search_item.html', context)                                  
    
    
def create_task(request):
    todo_form = TodoForm()

    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('home')
    
    context = {'todo_form': todo_form}
    return render(request, 'lists/create_task.html', context)


def info(request):
    all_count = Tasks.objects.all().count()
    personal_count = Tasks.objects.filter(purpose='Personal').count
    fitness_count = Tasks.objects.filter(purpose='Fitness').count
    school_count = Tasks.objects.filter(purpose='School').count
    business_count = Tasks.objects.filter(purpose='Business').count
    office_count = Tasks.objects.filter(purpose='Office').count
    completed_count = Tasks.objects.filter(completed=True).count
    
    context = {
        'all_count': all_count,
        'personal_count': personal_count,
        'fitness_count': fitness_count,
        'school_count': school_count,
        'business_count': business_count,
        'office_count': office_count,
        'completed_count': completed_count
        }
    
    return render(request, 'lists/info.html', context)


def update_task(request, slug):
    task = Tasks.objects.get(slug=slug)
    todo_form = TodoForm(instance=task)
    task_created = task.date_created
    
    
    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=task)
        if todo_form.is_valid():
            todo_form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    

    context = {'todo_form': todo_form, 'task_created': task_created}
    return render(request, 'lists/update_task.html', context)


def back_button(request):
    return redirect(request.META.get('HTTP_REFERER'))


def delete_task(request, slug):
    task = Tasks.objects.get(slug=slug)
    todo_form = TodoForm(instance=task)

    if request.method == 'POST':
        task.delete()
        next = request.POST.get('next', '/')        
        return HttpResponseRedirect(next)

    context = {'todo_form': todo_form}
    return render(request, 'lists/delete_task.html', context)


def personal(request):
    personal_items = Tasks.objects.filter(purpose='Personal').all()
    personal_count = Tasks.objects.filter(purpose='Personal').count()
    completed_count = Tasks.objects.filter(purpose='Personal').filter(completed=True).count()
    completed = Tasks.objects.filter(purpose='Personal').filter(completed=True).all().order_by('id') 
    
    context = {'personal_items': personal_items, 'personal_count': personal_count, 'completed': completed, 'completed_count': completed_count}
    return render(request, 'lists/personal.html', context)


def fitness(request):
    fitness_items = Tasks.objects.filter(purpose='Fitness').all()
    fitness_count = Tasks.objects.filter(purpose='Fitness').count()
    completed_count = Tasks.objects.filter(purpose='Fitness').filter(completed=True).count()
    completed = Tasks.objects.filter(purpose='Fitness').filter(completed=True).all().order_by('id')  
    
    context = {'fitness_items': fitness_items, 'fitness_count': fitness_count, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/fitness.html', context)

    
def school(request):
    school_items = Tasks.objects.filter(purpose='School').all()
    school_count = Tasks.objects.filter(purpose='School').count()
    completed_count = Tasks.objects.filter(purpose='School').filter(completed=True).count()
    completed = Tasks.objects.filter(purpose='School').filter(completed=True).all().order_by('id') 
    
    context = {'school_items': school_items, 'school_count': school_count, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/school.html', context)

    
def business(request):
    business_items = Tasks.objects.filter(purpose='Business').all()
    business_count = Tasks.objects.filter(purpose='Business').count()
    completed_count = Tasks.objects.filter(purpose='Business').filter(completed=True).count()
    completed = Tasks.objects.filter(purpose='Business').filter(completed=True).all().order_by('id')    
    
    context = {'business_items': business_items, 'business_count': business_count, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/business.html', context)

    
def office(request):
    office_items = Tasks.objects.filter(purpose='Office').all()
    office_count = Tasks.objects.filter(purpose='Office').count()
    completed_count = Tasks.objects.filter(purpose='Office').filter(completed=True).count()
    completed = Tasks.objects.filter(purpose='Office').filter(completed=True).all().order_by('id')       
    
    context = {'office_items': office_items, 'office_count': office_count, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/office.html', context)

