from django.db import models
from django.utils import timezone

import datetime
# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.TextField(max_length=200)
    votes=models.ImageField(default=0)

    def __str__(self):
        return self.choice_text