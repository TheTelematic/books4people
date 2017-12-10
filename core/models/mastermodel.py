from django.db import models

from core.managers.mastermanager import MasterManager


class MasterModel(models.Model):
    deleted = models.BooleanField(default=False)

    objects = MasterManager()

    def delete(self, using=None):
        self.deleted = True

        self.save()
