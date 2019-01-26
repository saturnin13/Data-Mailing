import re
from collections import Counter, OrderedDict

from mail_app.mail import Mail
from mail_app.mail_postprocessor.abstract_postprocessor import AbstractPostprocessor
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.postprocessed_mails import PostprocessedMails
from mail_app.processed_mail import ProcessedMail

class EmailPopularityPostprocessor(AbstractPostprocessor):

    general_keywords = ["interview", "application status", "follow up", "take home test", "next stage",
                        "your application", "thank you for applying"]

    def __init__(self):
        super().__init__()
        self.category = "Email popularity"

    def postprocess_all_mails(self, mails):
        froms = [mail.from_ for mail in mails]
        occurence_ordered_from = list(OrderedDict.fromkeys((sorted(froms, key=Counter(froms).get, reverse=True))))
        return PostprocessedMails(self.category, occurence_ordered_from)
