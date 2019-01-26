import string


class PostprocessedMails:

    def __init__(self, category: string, description: string, specifics: object = None):
        self.category = category
        self.description = description
        self.specifics = specifics

