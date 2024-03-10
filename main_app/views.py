from django.shortcuts import render
from .models import Trash

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trash_index(request):
  trash = Trash.objects.all()
  return render(request, 'trash/index.html', {'trashed': trash})

def trash_detail(request, trash_id):
  trash = Trash.objects.get(id=trash_id)
  return render(request, 'trash/detail.html', { 'trashed': trash})