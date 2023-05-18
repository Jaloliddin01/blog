from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.id} Lesson. {self.title.upper()}"
    
    class Meta:
        verbose_name = "Darsliklar".upper()

class Exercise(models.Model):
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Mashqlar".upper()
