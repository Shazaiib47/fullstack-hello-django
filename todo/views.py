from django.shortcuts import render

# Create your views here.
def get_todo__list(request):
    return render(request, 'todo/todo_list.html')
