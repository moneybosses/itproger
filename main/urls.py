
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('team/<int:member_id>/', views.team_member_detail, name='team_member_detail'),
    path('contact/', views.contact, name='contact')
]