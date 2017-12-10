from django.db import models


class MasterManager(models.Manager):
    def get_queryset(self):
        return super(MasterManager, self).get_queryset().filter(deleted=False)


class FullManager(models.Manager):
    def get_queryset(self):
        return super(FullManager, self).get_queryset()
