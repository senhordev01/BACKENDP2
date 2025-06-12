from django.shortcuts import render
from .models import Todo
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

class TodoListView(ListView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("todo_list")

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("todo_list")
    
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
