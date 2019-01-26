import datetime
import string


class ProcessedMail:

    def __init__(self, category: string, description: string, date: datetime, attachments: [string],
                 specifics: object = None):
        self.category = category
        self.description = description
        self.date = date
        self.attachments = attachments
        self.specifics = specifics

