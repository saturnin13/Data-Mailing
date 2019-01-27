import datetime
import string


class Mail:

    def __init__(self, user_id: string, message_id: string, from_: string, subject: string, body: string, attachments: [object], time: datetime):
        self.user_id = user_id
        self.message_id = message_id
        self.from_ = from_
        self.subject = subject
        self.body = body
        self.attachments = attachments
        self.time = time