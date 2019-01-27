import json
import re

from bs4 import BeautifulSoup

from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.processed_mail import ProcessedMail


class TicketProcessor(AbstractProcessor):

    general_keywords = ["boarding pass", "boardingpass", "booking reference", "ticket"]
    ticket_keyword = ["qrcode"]

    def __init__(self):
        super().__init__()
        self.category = "Ticket"

    def process(self, mail: Mail) -> ProcessedMail:
        if self.__general_conditions(mail):
            soup = BeautifulSoup(mail.body, 'html.parser')
            schema_script = soup.find('script', type="application/ld+json")
            if schema_script and schema_script.text:
                schema_json = json.loads(schema_script.text.replace('\\n', '').replace('\\r', '').strip())
                processed_mail = ProcessedMail(mail.user_id, mail.message_id, mail.from_, category=self.category,
                                               description=schema_json['reservationFor']['name'],
                                               date=mail.time, attachments=mail.attachments, specifics=schema_json)
                attrs = vars(processed_mail)
                return processed_mail
            return ProcessedMail(mail.user_id, mail.message_id, mail.from_, self.category, mail.body, mail.time, mail.attachments)

    ############################################ Conditions ############################################

    def __general_conditions(self, mail: Mail):
        return (mail.attachments or
                any(re.search(keyword, mail.body.lower()) for keyword in self.ticket_keyword)) and \
               (any(re.search(keyword, mail.subject.lower()) for keyword in self.general_keywords) or
                any(re.search(keyword, mail.body.lower()) for keyword in self.general_keywords) or
                any(re.search(keyword, name.lower()) for name, _ in mail.attachments.items() for keyword in
                    self.general_keywords))
