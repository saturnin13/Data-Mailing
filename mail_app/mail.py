class Mail:

    def __init__(self, from_, to_, subjects, body, attachments, time):
        self.from_ = from_
        self.to_ = to_
        self.subjects = subjects
        self.body = body
        self.attachments = attachments
        self.time = time

