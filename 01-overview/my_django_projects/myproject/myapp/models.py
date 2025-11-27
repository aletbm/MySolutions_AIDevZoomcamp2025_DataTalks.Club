from django.db import models

# Create your models here.                                                                                   
                                                                                                                
class Todo(models.Model):                                                                                  
    task = models.CharField(max_length=200)  # The description of the to-do item                               
    completed = models.BooleanField(default=False) # Whether the task is completed                             
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when created                              
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when last updated                             
                                                                                                                
    def __str__(self):                        
        return self.task              