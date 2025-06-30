from django.urls import reverse_lazy
from .forms import TodoForm
from .models import Todo
from django.views.generic import ListView as listview, CreateView as createview, UpdateView as updateview, DeleteView as deletview
# Create your views here.
class TodoListView(listview):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
class TodoCreateView(createview):
    model = Todo
    template_name = 'todo/todo_create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
class TodoUpdateView(updateview):
    model = Todo

    template_name = 'todo/todo_update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
class TodoDeleteView(deletview):
     model = Todo
     template_name = 'todo/todo_delete.html'
     success_url = reverse_lazy('todo_list')