from django.db import models

from core.managers.mastermanager import MasterManager, FullManager


class MasterModel(models.Model):
    deleted = models.BooleanField(default=False)

    objects = MasterManager()
    all_objects = FullManager()

    class Meta:
        abstract = True

    def delete(self, using=None):
        self.deleted = True

        self.save()
