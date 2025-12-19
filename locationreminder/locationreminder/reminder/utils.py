# reminder/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_reminder_email(reminder, distance_m=None):
    subject = f"Location Reminder: {reminder.title}"
    message = f"Reminder: {reminder.title}\nTarget: {reminder.target_lat}, {reminder.target_lon}\n"
    if distance_m is not None:
        message += f"Distance: {int(distance_m)} meters\n"
    message += "\n-- LocationReminder App"
    from_email = settings.EMAIL_HOST_USER or None
    send_mail(subject, message, from_email, [reminder.email], fail_silently=False)
