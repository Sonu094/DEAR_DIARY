from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Entry{self.id}') 