from django.db import models


class ProcessedEmail(models.Model):
    user_id = models.CharField(primary_key=True, max_length=1000)
    date = models.DateTimeField(max_length=1000)
    sender = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    attachment_location = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)

    @staticmethod
    def to_list_display():
        return ['user_id', 'date', 'sender', 'description', 'attachment_location', 'category']

    @staticmethod
    def to_list_filter():
        return []

    @staticmethod
    def search_fields():
        return []

