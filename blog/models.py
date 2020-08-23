from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CV(models.Model):
    author = models.CharField(max_length=100)
    Number = models.CharField(max_length=11, default='xxxxxxxxxxx')
    Email = models.CharField(max_length=50, default='example@domain.com')
    Date_of_birth = models.CharField(max_length=30)
    published_date = models.DateTimeField(blank=True, null=True)
    Personal_Profile = models.TextField()
    Education = models.TextField()
    Employment_History = models.TextField()
    Achievements = models.TextField()
    Interests = models.TextField()
    Skills = models.TextField()
    References = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author

class CV2(models.Model):
    author = models.CharField(max_length=100)
    Number = models.CharField(max_length=11, default='xxxxxxxxxxx')
    Email = models.CharField(max_length=50, default='example@domain.com')
    Date_of_birth = models.CharField(max_length=30, default='xx/xx/xxxx')
    published_date = models.DateTimeField(blank=True, null=True)
    Personal_Profile = models.TextField()
    Education = models.TextField()
    Employment_History = models.TextField()
    Achievements = models.TextField()
    Interests = models.TextField()
    Skills = models.TextField()
    References = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
