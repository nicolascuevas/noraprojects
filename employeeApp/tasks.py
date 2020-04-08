from noraprojects.celery_app import app
from noraprojects.settings import SLACK_CHANNEL, SLACK_TOKEN, SLACK_TEXT, MENU_URL
from slackclient import SlackClient
from employeeApp.models import Employee
from helpers import generate_uuid
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
    users = Employee.objects.all()
    for user in users:
        print (user)
        send_slack_message.delay(user.identifier)


@app.task
def send_slack_message(identifier):
    sc = SlackClient(SLACK_TOKEN)
    today_menu_url = MENU_URL.format(identifier)
    menu_description = "informacion del menu"
    menu_text = SLACK_TEXT.format(menu_description, today_menu_url)

    sc.api_call(
        "chat.postMessage",
        channel="UKUGXSH0V",
        text=menu_text
    )


