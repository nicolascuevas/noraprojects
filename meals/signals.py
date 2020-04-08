
from django.contrib.auth.models import Group
from employeeApp.tasks import reminder_slack_users,import_slack_users



def assign_admin_role(sender, instance, created, **kwargs):
    if created:
        print import_slack_users.delay()
        print reminder_slack_users.delay()
