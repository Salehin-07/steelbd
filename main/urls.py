from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("team/", views.team, name="team"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path('contact-messages/', views.show_contact_message, name='show_contact_messages'),
    path('toggle-message-status/<int:message_id>/', views.toggle_message_status, name='toggle_message_status'),
    
]
