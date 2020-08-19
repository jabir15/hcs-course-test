from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class LoginLogoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_login_time = models.DateTimeField(blank=True, default=timezone.now)
    last_logout_time = models.DateTimeField(blank=True, default=timezone.now)
    total_online_time = models.DurationField()

    def __str__(self):
        return self.user.username+'\'s hours'


class Standard(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    which_class = models.ForeignKey(Standard, on_delete=models.CASCADE)
    def __str__(self):
        return self.which_class.name+"-"+self.name


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    which_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    which_class = models.ForeignKey(Standard, on_delete=models.CASCADE)
    def __str__(self):
        return self.which_class.name+"-"+self.which_subject.name+":"+self.name

class Topic(models.Model):
    lesson = models.CharField(max_length=400)
    video = models.CharField(max_length=15, blank=True)
    which_chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    which_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    which_class = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return (self.which_class.name+":"
                +self.which_subject.name+"--"
                +self.which_chapter.name+" - "
                +self.lesson)


# from . import signals_handler
