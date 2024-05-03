from django.urls import path
from . import views




urlpatterns = [
    path('', views.homepage, name='home'),
    path('inser',views.insert,name='insert'),
    path('read',views.read, name='read'),
    path('update/<int:student_id>', views.update, name='update'),
    path('delete/<int:pk>',views.delete, name='delete'),
    path('sure/<int:pk>', views.sure, name='sure'),
]