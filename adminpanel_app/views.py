from django.shortcuts import render,redirect
from django.contrib import messages
from redirection.models import Visits
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncHour
from datetime import datetime,timedelta
from django.http import JsonResponse


# Create your views here.

def index(request):

    if 'email' not in request.session:
        messages.error(request, 'Login Required')
        return redirect('/auth/login/')
    
    today=timezone.now().date()
    total=Visits.objects.filter(unique_link=request.session['unique_link']).count()
    visits_today = Visits.objects.filter(timestamp__date=today).annotate(hour=TruncHour('timestamp')).values('hour').annotate(count=Count('id')).order_by('hour')

    hours = [f"{hour:02}:00" for hour in range(24)]
    counts = [0] * 24
    for visit in visits_today:
        hour = visit['hour'].hour
        counts[hour] = visit['count']

    top_cities=Visits.objects.filter(unique_link=request.session['unique_link']).values('city').annotate(count=Count('id')).order_by('-count')[:5]
    top_countries=Visits.objects.filter(unique_link=request.session['unique_link']).values('country').annotate(count=Count('id')).order_by('-count')[:5]

    print(top_cities)
    print(top_countries)

    context={
        'top_cities': top_cities,
        'top_countries': top_countries,
        'total_visits_day': sum(counts),
        'visits_per_hour': counts,
        'total_visits': total
    }
    return render(request,'dashboard.html',context)

def get_week_data(request):
    week_start = request.GET.get('week_start', None)
    if week_start:
        week_start = timezone.make_aware(datetime.strptime(week_start, '%Y-%m-%d'))
    else:
        today = timezone.now().date()
        week_start = today - timedelta(days=today.weekday())
        week_start = timezone.make_aware(datetime.combine(week_start, datetime.min.time()))


    week_end = week_start + timedelta(days=6)

    visits = Visits.objects.filter(timestamp__range=[week_start, week_end])

    visit_data = {week_start + timedelta(days=i): 0 for i in range(7)}

    for visit in visits:
        date = visit.timestamp.date()
        if date not in visit_data:
            visit_data[date] = 0  
        visit_data[date] += 1

    result={
        'labels': [date.strftime('%Y-%m-%d') for date in visit_data.keys()],
        'data': list(visit_data.values())
    }

    # fianl={}
    # for i in data:
    #     if i.timestamp.strftime('%Y-%m-%d') in fianl:
    #         fianl[i.timestamp.strftime('%Y-%m-%d')]+=1
    #     else:
    #         fianl[i.timestamp.strftime('%Y-%m-%d')]=1
    print(result)
    return JsonResponse(result)
        