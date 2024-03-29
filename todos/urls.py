from django.urls import path
from todos import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('todos/', views.Todos_api),
    path('todos/<int:pk>', views.Todos_api)
]

urlpatterns += staticfiles_urlpatterns()
