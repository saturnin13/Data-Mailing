import string


class PostprocessedMails:

    def __init__(self, category: string, specifics: object = None):
        self.category = category
        self.specifics = specifics

