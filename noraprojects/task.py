from settings import SLACK_CHANNEL, SLACK_TOKEN, SLACK_TEXT, MENU_URL
from celery_app import app
from noraprojects.settings import SLACK_CHANNEL, SLACK_TOKEN, SLACK_TEXT, MENU_URL
from slackclient import SlackClient
from meals.models import Menu, Option
from datetime import timedelta
from meals.helpers import generate_uuid
import datetime
import json
import uuid


@app.task
def send_slack_notification(uuid):
    slack_client = SlackClient(SLACK_TOKEN)
    menu_description = "El Menu para hoy es: \n"
    if len(Menu.objects.filter(uuid=uuid)) > 0:
        current_menu = Menu.objects.get(uuid=uuid)
        #we get the options from the menu
        menu_options = options = Option.objects.filter(menu__id=current_menu.id)
        for current_option in menu_options:
            menu_description += str(current_option.description) + "\n"

    today_menu_url = MENU_URL.format(uuid)
    menu_text = SLACK_TEXT.format(menu_description, today_menu_url)

    print(today_menu_url)
    print(menu_text)
    slack_client.api_call(
        "chat.postMessage",
        channel=SLACK_CHANNEL,
        text=menu_text
    )
