from django.db import models


class ProcessedEmail(models.Model):
    message_id = models.CharField(primary_key=True, max_length=1000)
    user_id = models.CharField(max_length=1000)
    date = models.DateTimeField(max_length=1000)
    sender = models.CharField(max_length=1000)
    description = models.TextField()
    attachment_location = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)

    @staticmethod
    def to_list_display():
        return ['user_id', 'message_id', 'date', 'sender', 'attachment_location', 'category']

    @staticmethod
    def to_list_filter():
        return []

    @staticmethod
    def search_fields():
        return []

