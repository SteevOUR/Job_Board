from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('s/', views.job_list, name='job_list'),
    path('-add/', views.add_job, name='add_job'),
    path('-<str:slug>-<int:id>/', views.job_detail, name='job_detail'),
]
