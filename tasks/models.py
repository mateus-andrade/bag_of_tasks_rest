from django.db import models
from django.contrib.postgres.fields import ArrayField

class Key(models.Model):
    line = models.IntegerField()
    column = models.IntegerField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE)


class Task(models.Model):
    STATE_CHOICES=(
        ('AVAILABLE', 'Available'),
        ('DONE', 'Done')
    )

    value = ArrayField(ArrayField(models.IntegerField(),size=3),size=3)
    state = models.CharField(choices=STATE_CHOICES, default='AVAILABLE',
                             max_length=9)


class KernelMatrix(models.Model):
    value = ArrayField(ArrayField(models.IntegerField(),size=3),size=3)
