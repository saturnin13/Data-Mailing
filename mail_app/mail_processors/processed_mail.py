import datetime
import string


class ProcessedMail:

    def __init__(self, category: string, original_mail_link: string, description: string, date: datetime, attachments: [string], specifics: object) -> object:
        self.category = category
        self.original_mail_link = original_mail_link
        self.description = description
        self.date = date
        self.attachments = attachments
        self.specifics = specifics

