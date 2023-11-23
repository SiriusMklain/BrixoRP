from django.shortcuts import render
from .models import *
from pathlib import Path
from .models import *


def app2(request):
    users = UserProfile.objects.all()
    reports_users = VisitToTT.objects.filter(month='2023-11-22').values(
        'user_profile__user__username',
        'user_profile__photo',
        'user_profile__workplace',
        'visits',
        'retail',
        'sto',
        'retail_buy_SAKURA_and_have',
        'sto_buy_SAKURA_and_have',
        'sto_dont_buy_SAKURA_and_have',
        'retail_dont_buy_SAKURA_and_have',
        'month',
        'id')

    text_sliders_dict = []

    for i in reports_users:
        text_sliders = TextSlide.objects.filter(visit_id=i['id']).values('title', 'text')
        text_sliders_dict.append({'id': i['id'], 'text_sliders': text_sliders})

    context = {
        'reports_users': reports_users,
        'text_sliders_dict': text_sliders_dict,
    }
    print(text_sliders_dict)


    return render(request, 'app2/index.html', context=context)
