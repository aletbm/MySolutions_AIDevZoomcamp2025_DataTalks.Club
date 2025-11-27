from django.shortcuts import render, redirect                                                                     
from .models import Todo                                                                                      
from .forms import TodoForm

# Create your views here.

def add_todo(request):                                                                                             
    if request.method == 'POST':                                                                                   
        form = TodoForm(request.POST)                                                                             
        if form.is_valid():                                                                                        
            form.save()                                                                                          
            return redirect('home')                                                                          
    else:                                                            
        form = TodoForm()                                              
    return render(request, 'myapp/add_todo.html', {'form': form})                                                 
                                                                                                                
def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)                                                                           
    if todo:                                            
        todo.completed = True                                                                                     
        todo.save()                                                                             
    return redirect('home')                                                                                  
                                                                                                                
def delete_todo(request, todo_id):                                                               
    todo = Todo.objects.get(id=todo_id)                                                                           
    if todo:                                                                                                      
        todo.delete()                                                  
    return redirect('home')

def home_view(request):                                                                                        
    """
    Renders the home page template.                                                                            
    """
    todos = Todo.objects.all()
    return render(request, 'myapp/home.html', {'todos': todos})