from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_home, name='event_home'),
    path('technical/', views.technical_events, name='technical_events'),
    path('non-technical/', views.non_technical_events, name='non_technical_events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]