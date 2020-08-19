import csv
from django.core.management.base import BaseCommand
from course.models import Standard, Subject, Chapter, Topic

def add_topics(wcls, wsub, wchap):
    """
    Add topics for a particular chapter of a subject in a class

    """
    #<Standard: Class 12>
    cls_name = Standard.objects.get(name=wcls)
    #<Subject: Class 12-Chemistry>
    sub_name = Subject.objects.filter(name=wsub).filter(which_class=cls_name).get()
    #<Chapter: Class 12-Chemistry:Haloalkanes and Haloarenes>
    chap_name = (Chapter.objects
                 .filter(name=wchap)
                 .filter(which_subject=sub_name)
                 .filter(which_class=cls_name)
                 .get())
    with open('filenames.csv', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in rows:
            topic = Topic(
                lesson=row[0],
                video=row[1],
                which_chapter=chap_name,
                which_subject=sub_name,
                which_class=cls_name)
            topic.save()

class Command(BaseCommand):
    """
    manage.py command to add topics from a csv file
    with lesson name and video id

    python manage.py addtopics -c "Class 12" -s "Physics" -ch "Nuclie"
    """
    help = 'Add topics by chapter, subject and class'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--class', help='Define which chapter',)
        parser.add_argument('-s', '--subject', help='Define which subject',)
        parser.add_argument('-ch', '--chapter', help='Define which chapter',)

    def handle(self, *args, **kwargs):
        wcls = kwargs['class']
        wsub = kwargs['subject']
        wchap = kwargs['chapter']

        add_topics(wcls, wsub, wchap)
        self.stdout.write(self.style.SUCCESS('Successfully added topics in "%s : %s -- %s"' \
            % (wcls, wsub, wchap)))
