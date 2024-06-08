from django.urls import path
from . import views

urlpatterns = [
    path('', views.UnderWorkView.as_view(), name='under-work'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('under-work/', views.UnderWorkView.as_view(), name='under-work'),
]