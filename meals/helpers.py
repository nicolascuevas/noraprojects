import uuid
from django.utils import timezone
from datetime import datetime, time


def generate_uuid():
    return uuid.uuid4().hex


def before_lunch_time(value):
    current_local_time = timezone.make_aware(datetime.now(),timezone.get_default_timezone())
    menu_local_time = timezone.make_aware(datetime.now(),timezone.get_default_timezone())
    menu_local_time = menu_local_time.replace(  
                                year=int(value.strftime('%Y')), 
                                month=int(value.strftime('%m')), 
                                day=int(value.strftime('%d')), 
                                hour=11, 
                                minute=0, 
                                second=0)

    return current_local_time < menu_local_time
    