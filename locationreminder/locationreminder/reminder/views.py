# reminder/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from math import radians, cos, sin, asin, sqrt
from .models import Reminder
from django.conf import settings

# ---------------- Landing / Auth ----------------
def project_info(request):
    return render(request, 'project_info.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created — please login")
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Direct to home page after login
        messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('project_info')


# ---------------- Home / Create / List ----------------
@login_required
def home(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'reminders': reminders})


@login_required
def save_reminder(request, reminder_id=None):
    if request.method == 'POST':
        title = request.POST.get('title')
        email = request.POST.get('email')
        lat = float(request.POST.get('lat'))
        lon = float(request.POST.get('lon'))
        radius = int(request.POST.get('radius') or 500)

        if reminder_id:
            reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
            reminder.title = title
            reminder.email = email
            reminder.target_lat = lat
            reminder.target_lon = lon
            reminder.radius = radius
            reminder.triggered = False  # reset triggered
            reminder.save()
            messages.success(request, "Reminder updated successfully!")
        else:
            Reminder.objects.create(
                user=request.user,
                title=title,
                email=email,
                target_lat=lat,
                target_lon=lon,
                radius=radius,
            )
            messages.success(request, "Reminder saved successfully!")

        return redirect('home')

    # GET request for editing
    reminder = None
    if reminder_id:
        reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    return render(request, 'home.html', {'reminder': reminder})


@login_required
def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == 'POST':
        reminder.title = request.POST.get('title')
        reminder.email = request.POST.get('email')
        reminder.target_lat = float(request.POST.get('lat'))
        reminder.target_lon = float(request.POST.get('lon'))
        reminder.radius = int(request.POST.get('radius'))
        reminder.triggered = False  # reset triggered
        reminder.save()
        return redirect('home')
    return render(request, 'edit_reminder.html', {'reminder': reminder})


@login_required
def delete_reminder(request, reminder_id):
    r = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    r.delete()
    messages.success(request, "Reminder deleted.")
    return redirect('home')


# ---------------- Tracking / Check endpoint ----------------
def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points in meters."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371000  # Earth radius in meters
    return c * r

@login_required
def check_location(request):
    """POST endpoint to check current location and trigger reminders."""
    if request.method != "POST":
        return JsonResponse({'triggered': False, 'message': 'Invalid request method'})

    try:
        lat = float(request.POST.get('lat'))
        lon = float(request.POST.get('lon'))
    except (TypeError, ValueError):
        return JsonResponse({'triggered': False, 'message': 'Invalid coordinates'})

    triggered_any = False
    message = ""

    reminders = Reminder.objects.filter(user=request.user)
    for r in reminders:
        distance = haversine(lat, lon, r.target_lat, r.target_lon)
        if distance <= r.radius:
            if not r.triggered:
                # Send email
                subject = f"Reminder: {r.title}"
                body = f"You reached the location for this reminder!\n\nTitle: {r.title}\nLatitude: {r.target_lat}\nLongitude: {r.target_lon}"
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,  # Must be set in settings.py
                    [r.email],
                    fail_silently=False,
                )
                r.triggered = True
                r.save()
                triggered_any = True
                message += f"Reminder triggered: {r.title}\n"

    if triggered_any:
        return JsonResponse({'triggered': True, 'message': message.strip()})
    return JsonResponse({'triggered': False, 'message': 'No reminder triggered'})


# ---------------- Optional: JSON API ----------------
@login_required
def api_reminders(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('-created_at')
    data = [{
        'id': r.id,
        'title': r.title,
        'email': r.email,
        'lat': r.target_lat,
        'lon': r.target_lon,
        'radius': r.radius,
        'triggered': r.triggered
    } for r in reminders]
    return JsonResponse({'reminders': data})
