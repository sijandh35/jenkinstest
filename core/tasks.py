from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
from pathlib import Path
import ftplib
from django.contrib.auth.models import User
import requests
import json
from core.models import StockLog, StockName

@shared_task(max_retries=1, soft_time_limit=600)
def stock_data_fetch(minutes=2):
    r = requests.get('https://nepse-data-api.herokuapp.com/data/todaysprice', params=request.GET)
    data = r.json()
    for v in StockName.objects.all():
        f = filter(lambda d: d['companyName'] == v.name ,data)
        v.log.create(json=json.dumps(list(f)[0]),stock_name=v.name)
    return True