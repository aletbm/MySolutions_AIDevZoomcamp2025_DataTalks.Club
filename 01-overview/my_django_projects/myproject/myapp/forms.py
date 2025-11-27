from django import forms                                                                                       
from .models import Todo                                                                                       
                                                                                                                   
class TodoForm(forms.ModelForm):                                                                                  
    class Meta:                                                                                                   
        # This tells Django to create a form based on the Todo model.                                             
        model = Todo                                                                                              
        # 'fields' specifies which fields from the model should be included in the form.                          
        # We want to include 'task' and 'completed'.                                                              
        fields = ['task', 'completed']