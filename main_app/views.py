from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trash
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

@login_required
def trash_index(request):
  trash = Trash.objects.filter(user=request.user)
  return render(request, 'trash/index.html', {'trashed': trash})

@login_required
def trash_detail(request, trash_id):
  trash = Trash.objects.get(id=trash_id)
  return render(request, 'trash/detail.html', { 'trashed': trash})


class TrashCreate(LoginRequiredMixin, CreateView):
  model = Trash
  fields = '__all__'
  success_url = '/trash/'
  def form_value(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TrashUpdate(LoginRequiredMixin, UpdateView):
  model = Trash
  fields = ['type', 'description', 'piecesOfTrash']

class TrashDelete(LoginRequiredMixin, DeleteView):
  model = Trash
  success_url = '/trash/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('trash-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)