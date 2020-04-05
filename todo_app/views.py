from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionDenied


from todo_app.models import Task


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    template = 'todo_app/home.html'
    context = {
        'tasks': Task.objects.filter(author=request.user),
    }

    return render(request, template, context)


class CreatTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo_app/new_task.html'
    success_url = reverse_lazy('home')
    fields = ('text', )

    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo_app/edit_task.html'
    success_url = reverse_lazy('home')
    fields = ('text',)

    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo_app/delete_task.html'
    success_url = reverse_lazy('home')

    login_url = reverse_lazy('login')\


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
