from django.db import models

from books.models.bookmanager import BookManager


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    reference = models.CharField(max_length=50)
    edited_date = models.DateField()
    entered_time = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    objects = BookManager()

    def __unicode__(self):
        return "{} - {} ({})".format(self.title, self.author, self.reference)

    def delete(self, using=None):
        self.deleted = True

        self.save()
