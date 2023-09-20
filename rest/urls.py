from django.urls import path
from. import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('stud/',views.detail_view),
    path('create/', views.insert_data),
]