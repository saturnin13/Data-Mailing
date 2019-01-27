from django.db import models


class ProcessedEmail(models.Model):
    user_id = models.CharField(primary_key=True, max_length=1000)
    date = models.DateTimeField(max_length=1000)
    from_ = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    attachment_location = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)

