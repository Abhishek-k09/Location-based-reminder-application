from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'target_lat', 'target_lon', 'radius', 'triggered', 'created_at', 'user')
    list_filter = ('triggered','created_at')
    search_fields = ('title','email')
