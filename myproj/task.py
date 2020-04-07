from settings import SLACK_CHANNEL, SLACK_TOKEN, SLACK_TEXT, MENU_URL
from slackclient import SlackClient
from myproj.celery_app import app
from celery import shared_task


@shared_task
def send_slack_notification(option, uuid):
    slack_client = SlackClient(SLACK_TOKEN)

    menu_description = ''
    for current_option in option:
        menu_description += str(current_option.description) + "\n"
        #options.append(str(current_option.description))

    #menu_description = str(options)

    print(menu_description)

    today_menu_url = MENU_URL.format(uuid)
    menu_text = SLACK_TEXT.format(menu_description, today_menu_url)

    print(today_menu_url)
    print(menu_text)
    slack_client.api_call(
        "chat.postMessage",
        channel=SLACK_CHANNEL,
        text=menu_text
    )