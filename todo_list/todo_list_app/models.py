from django.db import models


class TodoItem(models.Model):
    value = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)