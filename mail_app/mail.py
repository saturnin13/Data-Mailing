class Mail:

    def __init__(self, from_: object, to_: object, subject: object, body: object, attachments: object, time: object) -> object:
        self.from_ = from_
        self.to_ = to_
        self.subject = subject
        self.body = body
        self.attachments = attachments
        self.time = time

