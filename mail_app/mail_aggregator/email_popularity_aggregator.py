from collections import Counter, OrderedDict

from mail_app.mail_aggregator.abstract_aggregator import AbstractAggregator
from mail_app.aggregated_mails import AggregatedMails


class EmailPopularityAggregator(AbstractAggregator):

    general_keywords = ["interview", "application status", "follow up", "take home test", "next stage",
                        "your application", "thank you for applying"]

    def __init__(self):
        super().__init__()
        self.category = "Email popularity"

    def postprocess_all_mails(self, mails):
        froms = [mail.from_ for mail in mails]
        occurence_ordered_from = list(OrderedDict.fromkeys((sorted(froms, key=Counter(froms).get, reverse=True))))
        return AggregatedMails(self.category, occurence_ordered_from)
