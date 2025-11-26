from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add-cycle/', views.add_cycle, name="add_cycle"),
    path('reset-cycles/', views.reset_cycles, name='reset_cycles'),

]
