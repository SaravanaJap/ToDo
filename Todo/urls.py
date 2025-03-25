from django.urls import path,include
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>',views.markComplete,name='markComplete'),
    path('mark_as_Undone/<int:pk>',views.markInComplete,name='markInComplete'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),

]