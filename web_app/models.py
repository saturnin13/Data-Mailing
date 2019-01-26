from django.db import models


class ProcessedEmail(models.Model):
    user_id = models.CharField()
    date = models.TimeField()
    from_ = models.CharField()
    description = models.CharField()
    attachment_location = models.CharField()
    category = models.CharField()

