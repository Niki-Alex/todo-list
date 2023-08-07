from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tag, Task


class HomePage(generic.ListView):
    model = Task
    template_name = "todo/home_page.html"


class ToggleAssignToTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        if task.completed:
            task.completed = False
        else:
            task.completed = True

        task.save()

        return redirect(reverse_lazy(
            "catalog:home-page"
        ))
