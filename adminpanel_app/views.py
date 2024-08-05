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
        return redirect('/auth/login/?redirection=/home/')
    
    
    today=timezone.now().date()
    total=Visits.objects.filter(unique_link=request.session['unique_link']).count()


    top_cities=Visits.objects.filter(unique_link=request.session['unique_link']).values('city').annotate(count=Count('id')).order_by('-count')[:5]
    top_countries=Visits.objects.filter(unique_link=request.session['unique_link']).values('country').annotate(count=Count('id')).order_by('-count')[:5]

    print(top_cities)
    print(top_countries)


    context={
        'top_cities': top_cities,
        'top_countries': top_countries,
        'total_visits': total
    }
    return render(request,'dashboard.html',context)

def get_week_data(request):
    if 'email' not in request.session:
        messages.error(request, 'Login Required')
        return redirect('/auth/login/')
    week_start = request.GET.get('week_start', None)
    if week_start:
        week_start = timezone.make_aware(datetime.strptime(week_start, '%Y-%m-%d'))
    else:
        today=timezone.now().date()
        week_start = today - timedelta(days=today.weekday())
        week_start = timezone.make_aware(datetime.combine(week_start, datetime.min.time()))


    week_end = week_start + timedelta(days=6, hours=23, minutes=59, seconds=59)

    visits = Visits.objects.filter(timestamp__range=[week_start, week_end])

    visit_data = {week_start.date() + timedelta(days=i): 0 for i in range(7)}


    for visit in visits:
        date = visit.timestamp.date()
        if date in visit_data:
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
        

def get_link(request):
    if 'email' not in request.session:
        messages.error(request, 'Login Required')
        return redirect('/auth/login/?redirection=/home/get_link/')
    
    unique_link=request.session['unique_link']

    context={
        'unique_link': unique_link
    }
    return render(request,'get_link.html',{'context':context})

def get_specific_day(request):
    if 'email' not in request.session:
        messages.error(request, 'Login Required')
        return redirect('/auth/login/')
    
    date_start = request.GET.get('date_start', None)
    if date_start:
        date_start = datetime.strptime(date_start, '%Y-%m-%d')
    else:
        date_start = timezone.now().date()

    visits_today = Visits.objects.filter(timestamp__date=date_start).annotate(hour=TruncHour('timestamp')).values('hour').annotate(count=Count('id')).order_by('hour')

    hours = [f"{hour:02}:00" for hour in range(24)]
    counts = [0] * 24

    for visit in visits_today:
            hour = visit['hour'].hour
            counts[hour] = visit['count']

    context={
        'total_visits_day': sum(counts),
        'visits_per_hour': counts,
    }

    print(context)

    return JsonResponse(context)

