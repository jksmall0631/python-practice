# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Todo

def todo_list(request):
    todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todos/todo_list.html', {'todos': todos})
