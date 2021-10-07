import calendar
from django.http.response import HttpResponseRedirect
from .forms import EventForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import Event
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        calendar = Calendar(d.year, d.month)
        html_cal = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
    
def event(request, event_id=None):
    instance= Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reversed('calendary:calendar'))
    return render(request, 'event.html', {'form': form})

def event_form(request):
    if request.method=="POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('event_form'))
        else:
            print(form.errors)
    else:
        form= EventForm()
    return render(request,"event_form.html",{"form":form})

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


# Create your views here.
