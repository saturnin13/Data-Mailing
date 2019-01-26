import string


class AggregatedMails:

    def __init__(self, category: string, specifics: object = None):
        self.category = category
        self.specifics = specifics

