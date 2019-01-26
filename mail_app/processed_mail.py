import datetime
import string


class ProcessedMail:

    def __init__(self, user_id: string, from_: string, category: string, description: string, date: datetime, attachments: [string],
                 specifics: object = None):
        self.user_id = user_id
        self.from_ = from_
        self.category = category
        self.description = description
        self.date = date
        self.attachments = attachments
        self.specifics = specifics

