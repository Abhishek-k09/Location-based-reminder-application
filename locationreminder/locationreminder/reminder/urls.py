# reminder/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_info, name='project_info'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('home/', views.home, name='home'),                    # main dashboard + create + list
    path('save-reminder/', views.save_reminder, name='save_reminder'),
    path('edit-reminder/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),

    path("delete-reminder/<int:reminder_id>/", views.delete_reminder, name="delete_reminder"),


    
    path('check-location/', views.check_location, name='check_location'),  # POST endpoint for geofence checks
    path('api/reminders/', views.api_reminders, name='api_reminders'),     # returns JSON list (optional)
]
