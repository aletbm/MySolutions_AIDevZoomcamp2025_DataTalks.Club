from django.urls import path                                                                                      
from . import views                                                                                               
                                                                                                                
urlpatterns = [                                                                                                   
    path('', views.home_view, name='home'),                                                           
     path('add/', views.add_todo, name='add_todo'),                                                                 
     path('complete/<int:todo_id>/', views.mark_complete, name='mark_complete'),                                            
     path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),     
 ]