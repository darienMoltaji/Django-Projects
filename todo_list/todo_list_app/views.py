from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# TODO Create a view that serves the todolist html page
# TODO Create a view to add to the database 
# TODO Create a view to remove from the database 
# TODO Create a view to edit TodoItem value
# TODO Create a view to check/uncheck TodoItem
# TODO models for all these
delete all this