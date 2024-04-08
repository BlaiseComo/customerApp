from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('preworkouts/', views.PreWorkoutListView.as_view(), name='preworkouts'),
    path('pre/<int:pk>/', views.PreWorkoutDetailView.as_view(), name='preworkout-detail'),

    path('create_preworkout/', views.create_preworkout, name="create_preworkout"),
    path('update_preworkout/<int:id>/', views.update_preworkout, name='update_preworkout'),
    path('delete/<int:id>/', views.delete_preworkout, name='delete_preworkout')
]