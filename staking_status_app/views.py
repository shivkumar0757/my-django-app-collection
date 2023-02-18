from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

from staking_status_app.staking_status_service import get_status
from staking_status_app.tasks import check_and_save_status, test_func
# Create your views here.

def index(request):
    st_data= get_status()
    return render(request,'index.html',{'data':st_data})

def status_view_job(request):
    # Schedule the Celery task to run in the background
    print('starting.. via api in view.')
    check_and_save_status()

    # test_func.delay()
    check_and_save_status.delay()
    print('started out...')

    # Return a response to the client
    return JsonResponse({'message': 'Status check scheduled'})