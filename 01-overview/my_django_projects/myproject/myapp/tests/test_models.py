from django.test import TestCase                                                                                  
from ..models import Todo                                                                                          
                                                                                                                
class TodoModelTestCase(TestCase):                                                                                
    """                                                                                                           
    Tests for the Todo model.                                                                                     
    """                                                                                                           
                                                                                                                
    def setUp(self):                                                                                              
        """                                                                                                       
        Set up test data that will be used across multiple test methods.                                          
        This method is called before each test method.                                                            
        """                                                                                                       
        self.todo_item_1 = Todo.objects.create(task="Buy groceries", completed=False)                            
        self.todo_item_2 = Todo.objects.create(task="Walk the dog", completed=True)                              
                                                                                                                
    def test_todo_creation(self):                                                                                 
        """                                                                                                       
        Test that a Todo item can be created successfully.                                                        
        """                                                                                                       
        # We already created items in setUp, so let's create one more to be explicit                              
        new_todo = Todo.objects.create(task="Learn Django testing", completed=False)                             
        self.assertEqual(new_todo.task, "Learn Django testing")                                                  
        self.assertFalse(new_todo.completed)                                                                      
        self.assertEqual(Todo.objects.count(), 3) # 2 from setUp + 1 new                                          
                                                                                                                
    def test_todo_defaults(self):                                                                                 
        """                                                                                                       
        Test that default values for fields are set correctly.                                                    
        Assuming 'completed' defaults to False if not provided.                                                   
        """                                                                                                       
        # If your model has default values, test them here.                                                       
        # For example, if 'completed' defaults to False:                                                          
        default_todo = Todo.objects.create(task="Default test")                                                  
        self.assertFalse(default_todo.completed)                                                                  
                                                                                                                
    def test_todo_str_representation(self):                                                                       
        """                                                                                                       
        Test the __str__ method of the Todo model.                                                                
        This ensures that the object is represented by its task when printed.                                    
        """                                                                                                       
        self.assertEqual(str(self.todo_item_1), "Buy groceries")                                                  
        self.assertEqual(str(self.todo_item_2), "Walk the dog")                                                   
                                                                                                                
    def test_todo_update(self):                                                                                   
        """                                                                                                       
        Test that a Todo item can be updated.                                                                     
        """                                                                                                       
        # Retrieve an item created in setUp                                                                       
        todo_to_update = Todo.objects.get(task="Buy groceries")                                                  
        todo_to_update.completed = True                                                                           
        todo_to_update.save()                                                                                     
                                                                                                                
        # Retrieve it again to confirm the update                                                                 
        updated_todo = Todo.objects.get(task="Buy groceries")                                                    
        self.assertTrue(updated_todo.completed)                                                                   
                                                                                                                
    def test_todo_deletion(self):                                                                                 
        """                                                                                                       
        Test that a Todo item can be deleted.                                                                     
        """                                                                                                       
        # Get the count before deletion                                                                           
        initial_count = Todo.objects.count()                                                                      
                                                                                                                
        # Get an item to delete                                                                                   
        todo_to_delete = Todo.objects.get(task="Walk the dog")                                                   
        todo_to_delete.delete()                                                                                   
                                                                                                                
        # Check if the count has decreased                                                                        
        self.assertEqual(Todo.objects.count(), initial_count - 1)                                                 
                                                                                                                
        # Verify the item is no longer in the database                                                            
        with self.assertRaises(Todo.DoesNotExist):                                                                
            Todo.objects.get(task="Walk the dog")                                                                

#python manage.py test myapp.tests.test_models.TodoModelTestCase