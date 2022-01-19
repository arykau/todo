from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from .forms import CreateForm, TaskForm

from django.contrib.auth.decorators import login_required


class LoginPage(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


@login_required
def home_page(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == 'GET':
        search_input = request.GET.get('search-area') or ''

        if search_input:
            tasks = tasks.filter(title__icontains=search_input)

    context = {'tasks': tasks, 'form': form, 'search': search_input}
    return render(request, 'todo/tasks.html', context)


def task_add(request):

    form = CreateForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todo/create.html', context)


def task_detail(request, pk):
    task = Task.objects.get(id=pk)

    context = {'task': task}
    return render(request, 'todo/description.html', context)


def task_update(request, pk):
    task = Task.objects.get(id=pk)

    form = CreateForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'todo/create.html', context)


def task_delete(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'todo/delete.html', context)
