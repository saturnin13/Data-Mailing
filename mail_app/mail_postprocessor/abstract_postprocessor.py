from abc import ABC, abstractmethod

from mail_app.mail import Mail
from mail_app.postprocessed_mails import PostprocessedMails


class AbstractPostprocessor(ABC):

    category = ""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self, mails: [Mail]) -> PostprocessedMails:
        pass