import json
import re

from bs4 import BeautifulSoup

from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.processed_mail import ProcessedMail


class TicketProcessor(AbstractProcessor):
    general_keywords = ["ticket", "boarding pass", "boardingpass", "booking reference"]
    ticket_keyword = ["qrcode"]

    def __init__(self):
        super().__init__()
        self.category = "Ticket"

    def process(self, mail: Mail) -> ProcessedMail:
        soup = BeautifulSoup(mail.body, 'html.parser')
        schema_script = soup.find('script', type="application/ld+json")
        if schema_script:
            schema_json = json.loads(schema_script.text)
            processed_mail = ProcessedMail(category=self.category, description=schema_json['reservationFor']['name'],
                                           date=mail.time, attachments=mail.attachments, specifics=schema_json)
            attrs = vars(processed_mail)
            print(', '.join("%s: %s" % item for item in attrs.items()))
            return processed_mail
        if self.__general_conditions(mail):
            return ProcessedMail(self.category, mail.body, mail.time, mail.attachments)

    ############################################ Conditions ############################################

    def __general_conditions(self, mail: Mail):
        return (mail.attachments or
                any(re.search(mail.body.lower(), keyword) for keyword in self.ticket_keyword)) and \
               (any(re.search(mail.subject.lower(), keyword) for keyword in self.general_keywords) or
                any(re.search(mail.body.lower(), keyword) for keyword in self.general_keywords) or
                any(re.search(attachment["name"].lower(), keyword) for attachment in mail.attachments for keyword in
                    self.general_keywords))
