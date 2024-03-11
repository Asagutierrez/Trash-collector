from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('trash/', views.trash_index, name='trash-index'),
  path('trash/<int:trash_id>/', views.trash_detail, name='trash-detail'),
  path('trash/create/', views.TrashCreate.as_view(), name='trash-create'),
  path('trash/<int:pk>/update/', views.TrashUpdate.as_view(), name='trash-update'),
  path('trash/<int:pk>/delete/', views.TrashDelete.as_view(), name='trash-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]