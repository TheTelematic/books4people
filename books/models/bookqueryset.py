from django.db import models


class BookQuerySet(models.QuerySet):
    def get_queryset(self):
        return super(BookQuerySet, self).filter(deleted=False)
