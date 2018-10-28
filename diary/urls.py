from django.urls import path

from diary import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
]
