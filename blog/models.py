from django.conf import settings
from django.db import models
from django.utils import timezone
from myutils import kst_datetime


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(
            default=timezone.now)
    create_kst_date = models.DateTimeField(
            default=kst_datetime)
    publish_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
