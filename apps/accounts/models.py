from django.db import models

from jobportal.apps.jobs.models import UserProfile, Plan


class RecruiterDetail(models.Model):
    user = models.ForeignKey(UserProfile)
    upgrade_confirm = models.BooleanField(default=False)
    plan = models.ForeignKey(Plan)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "RecruiterDetails"