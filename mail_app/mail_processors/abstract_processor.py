from abc import ABC, abstractmethod

from mail_app.mail import Mail
from mail_app.processed_mail import ProcessedMail


class AbstractProcessor(ABC):

    category = ""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self, mail: Mail) -> ProcessedMail:
        pass