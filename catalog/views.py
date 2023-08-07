from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tag, Task


class HomePage(generic.ListView):
    model = Task
    template_name = "todo/home_page.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


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
