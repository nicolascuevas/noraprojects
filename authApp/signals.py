from django.contrib.auth.models import Group



def assign_admin_role(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.filter(name__iexact='admin').first()
            instance.groups.add(group)
            instance.save()
        except Exception as exc:
            print(exc)
