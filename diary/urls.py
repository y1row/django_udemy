from django.urls import path

from diary import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
]
