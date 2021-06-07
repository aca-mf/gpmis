from django.db import models

class Executions(models.Model):
    exec_date = models.DateTimeField('execution date')
    result = models.TextField()


