from celery import shared_task


@shared_task
def import_contacts(arg1, arg2, be_careful=False):
    print("aaa", arg1, arg2, be_careful)


@shared_task
def import_contacts2():
    print("bbb")
