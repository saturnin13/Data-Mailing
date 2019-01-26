import datetime
import string


class Mail:

    def __init__(self, from_: string, to_: string, subject: string, body: string, attachments: [string], time: datetime) -> object:
        self.from_ = from_
        self.to_ = to_
        self.subject = subject
        self.body = body
        self.attachments = attachments
        self.time = time

