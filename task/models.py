from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(verbose_name="Дата выполнения", auto_now_add=True)

    def __str__(self):
        return self.title