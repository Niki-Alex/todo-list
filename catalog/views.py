from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tag, Task


class HomePage(generic.ListView):
    model = Task
    # template_name = "newspaper/redactor_list.html"
