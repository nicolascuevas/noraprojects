from noraprojects.celery_app import app
from noraprojects.settings import SLACK_CHANNEL, SLACK_TOKEN, SLACK_TEXT, MENU_URL
from slackclient import SlackClient
from employeeApp.models import Employee
from meals.models import Menu, Option

from helpers import generate_uuid
import datetime
import json
import uuid


@app.task
def prueba_suma(x, y):
    return x + y


@app.task
def import_slack_users():
    sc = SlackClient(SLACK_TOKEN)
    users = sc.api_call("users.list")
    users = json.dumps(users)
    users = json.loads(str(users))
    users = users["members"]
    for record in users:
        try:
            if record["deleted"] == False:
                new_user = Employee(
                    identifier= generate_uuid(),
                    name = record['real_name'],
                    slack_id = record['id'],
                )
                new_user.save()
                print (new_user.__str__())
            else:
                print ("no")
        except:
            print("error")

    return users


@app.task
def reminder_slack_users():
    current_date = datetime.datetime.now()
    year = current_date.strftime("%Y")
    month = current_date.strftime("%m")
    day = current_date.strftime("%d")
    if len(Menu.objects.filter(date__year=year, date__month=month, date__day=day)) > 0:
        current_menu = Menu.objects.filter(date__year=year, date__month=month, date__day=day)[0]
        #we get the options from the menu
        menu_options = options = Option.objects.filter(menu__id=current_menu.id)

        users = Employee.objects.all()
        menu_description = "El Menu para hoy es: \n"
        for current_option in menu_options:
            menu_description += str(current_option.description) + "\n"

        for user in users:
            print (user)
            send_slack_message.delay(user.identifier, menu_description)


@app.task
def send_slack_message(identifier, menu_description):
    sc = SlackClient(SLACK_TOKEN)
    today_menu_url = MENU_URL.format(identifier)
    menu_text = SLACK_TEXT.format(menu_description, today_menu_url)

    sc.api_call(
        "chat.postMessage",
        channel="UKUGXSH0V",
        text=menu_text
    )


