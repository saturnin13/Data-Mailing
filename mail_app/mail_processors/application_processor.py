import re

from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.processed_mail import ProcessedMail

class ApplicationProcessor(AbstractProcessor):

    general_keywords = ["interview", "application status", "follow up", "take home test", "next stage",
                        "your application", "thank you for applying"]

    def __init__(self):
        super().__init__()
        self.category = "Application"

    def process(self, mail):
        if self.__general_conditions(mail):
            return ProcessedMail(mail.user_id, mail.from_, self.category, mail.body, mail.time, mail.attachments)

    ############################################ Conditions ############################################

    def __general_conditions(self, mail: Mail):
        return mail.attachments and \
           (any(re.search(keyword, mail.subject.lower()) for keyword in self.general_keywords) or
            any(re.search(keyword, mail.body.lower()) for keyword in self.general_keywords) or
            any(re.search(keyword, attachment["name"].lower()) for attachment in mail.attachments for keyword in
                self.general_keywords))