import random

from django.db import models


# yes, this is dumb
def get_my_uuid():
    return random.randint(1, 999999)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    myuuid = models.PositiveIntegerField(default=get_my_uuid)
