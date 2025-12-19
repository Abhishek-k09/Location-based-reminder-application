from django.contrib import admin
from django.urls import path, include
from reminder import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Use app urls:
    path('', include('reminder.urls')),

    # OR if you prefer to map individually:
    # path('', views.project_info, name='project_info'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('home/', views.home, name='home'),
    # path('save-reminder/', views.save_reminder, name='save_reminder'),
    # path('check-location/', views.check_location, name='check_location'),
]
