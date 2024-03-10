from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('trash/', views.trash_index, name='trash-index'),
  path('trash/<int:trash_id>/', views.trash_detail, name='trash-detail')
]