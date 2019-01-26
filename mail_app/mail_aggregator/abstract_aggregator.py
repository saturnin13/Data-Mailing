from abc import ABC, abstractmethod

from mail_app.mail import Mail
from mail_app.aggregated_mails import AggregatedMails


class AbstractAggregator(ABC):

    category = ""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def aggregate_all_mails(self, mails: [Mail]) -> AggregatedMails:
        pass