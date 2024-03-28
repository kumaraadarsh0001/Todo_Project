from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.Todos_api),
    path('todos/<int:pk>', views.Todos_api)
]
