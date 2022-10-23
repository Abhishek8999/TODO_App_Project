from django.db import models
from django.contrib.auth.models import User
import calendar
from datetime import datetime
from django.db.models import Q
from django.utils import timezone


class TODO(models.Model):
    d_fmt = "{0:>02}.{1:>02}.{2}"
    status_choices = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending')
    ]
    title = models.CharField(max_length=50)
    details = models.CharField(max_length = 500)
    status = models.CharField(max_length=25 , choices=status_choices)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateTimeField(auto_now_add = False)

    def __str__(self):
        return self.title
