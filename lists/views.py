from django.shortcuts import render, redirect
from lists.models import Tasks
from lists.forms import TodoForm

# Create your views here.
def home(request):
    tasks = Tasks.objects.all()
    completed_count = Tasks.objects.all().filter(completed=True).count
    completed = Tasks.objects.all().filter(completed=True).all().order_by('id')
    
    context = {'tasks': tasks, 'completed_count': completed_count, 'completed': completed}
    return render(request, 'lists/home.html', context)


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
    all_count = Tasks.objects.all().count
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

    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=task)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('home')

    context = {'todo_form': todo_form}
    return render(request, 'lists/update_task.html', context)


def delete_task(request, slug):
    task = Tasks.objects.get(slug=slug)
    todo_form = TodoForm(instance=task)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'todo_form': todo_form}
    return render(request, 'lists/delete_task.html', context)


def personal(request):
    personal_items = Tasks.objects.filter(purpose='Personal').all
    context = {'personal_items': personal_items}
    return render(request, 'lists/personal.html', context)


def fitness(request):
    fitness_items = Tasks.objects.filter(purpose='Fitness').all
    context = {'fitness_items': fitness_items}
    return render(request, 'lists/fitness.html', context)

    
def school(request):
    school_items = Tasks.objects.filter(purpose='School').all
    context = {'school_items': school_items}
    return render(request, 'lists/school.html', context)

    
def business(request):
    business_items = Tasks.objects.filter(purpose='Business').all
    context = {'business_items': business_items}
    return render(request, 'lists/business.html', context)

    
def office(request):
    office_items = Tasks.objects.filter(purpose='Office').all
    context = {'office_items': office_items}
    return render(request, 'lists/office.html', context)

