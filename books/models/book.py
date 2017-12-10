from django.db import models

from core.models.mastermodel import MasterModel


class Book(MasterModel):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    reference = models.CharField(max_length=50)
    edited_date = models.DateField()
    entered_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{} - {} ({})".format(self.title, self.author, self.reference)
