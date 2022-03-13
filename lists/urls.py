from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_task', views.create_task, name='create-task'),
    path('info', views.info, name='info'),    
    path('personal_info', views.personal, name='personal-info'),    
    path('fitness_info', views.fitness, name='fitness-info'),    
    path('school_info', views.school, name='school-info'),    
    path('business_info', views.business, name='business-info'),    
    path('office_info', views.office, name='office-info'),    
    path('update_task/<slug:slug>', views.update_task, name='update-task'),
    path('delete_task/<slug:slug>', views.delete_task, name='delete-task'),
    path('search_item', views.search_item, name='search-item'),
]
