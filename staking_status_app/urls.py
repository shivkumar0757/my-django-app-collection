from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('start-status', views.status_view_job, name='start-status'),
]