from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from course.models import LoginLogoutLog

from django.utils import timezone
import csv

def log_teachers():
    qs = LoginLogoutLog.objects.all()
    with open('teachers.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(['Timestamp', 'userID', 'First Name', 'Last Name', 'Logged Time'])
        for q in qs:
            userID = q.user.username
            fn = q.user.first_name
            ln = q.user.last_name
            h, r = divmod(q.total_online_time.total_seconds(), 3600)
            m, s = divmod(r, 60)
            log_time = '{:02}:{:02}:{:02}'.format(int(h), int(m), int(s))
            writer.writerow([timezone.localtime(timezone.now()), userID, fn, ln, log_time])

class Command(BaseCommand):
    help = 'Logs the teachers total online time'

    def handle(self, **options):
        log_teachers()

