from django.shortcuts import render, get_object_or_404
from .models import Event

def event_home(request):
    return render(request, "event_home.html")

def technical_events(request):
    technical_events = Event.objects.filter(category='TECHNICAL')
    return render(request, "technical_events.html", {
        'technical_events': technical_events,
    })

def non_technical_events(request):
    non_technical_events = Event.objects.filter(category='NON_TECHNICAL')
    return render(request, "non_technical_events.html", {
        'non_technical_events': non_technical_events,
    })

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event_detail.html", {
        'event': event,
    })