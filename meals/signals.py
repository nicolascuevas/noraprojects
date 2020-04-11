from django.db.models.signals import post_save
from django.dispatch import receiver
from meals.models import Menu
from noraprojects.task import send_slack_notification
import datetime 
from django.utils import timezone


@receiver(post_save, sender=Menu)
def menu_saved(sender, instance, **kwargs):
    #set the reminder at 9 am of the menus date after de menu is created
    menu = instance
    time = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
    time = time.replace(   year=int(menu.date.strftime('%Y')), 
                                month=int(menu.date.strftime('%m')), 
                                day=int(menu.date.strftime('%d')), 
                                hour=9, 
                                minute=0, 
                                second=0)
    #set de reminder for a specific task in santiago's local time
    send_slack_notification.apply_async(args=[], kwargs={'uuid': menu.uuid}, eta=time)