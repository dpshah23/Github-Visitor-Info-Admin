from django.shortcuts import render
from redirection.models import Visits
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncHour


# Create your views here.

def index(request):
    today=timezone.now().date()
    total=Visits.objects.filter(unique_link=request.session['unique_link']).count()
    visits_today = Visits.objects.filter(timestamp__date=today).annotate(hour=TruncHour('timestamp')).values('hour').annotate(count=Count('id')).order_by('hour')

    hours = [f"{hour:02}:00" for hour in range(24)]
    counts = [0] * 24
    for visit in visits_today:
        hour = visit['hour'].hour
        counts[hour] = visit['count']
    context={
        'total_visits_day': sum(counts),
        'visits_per_hour': counts,
        'total_visits': total
    }
    return render(request,'dashboard.html',context)