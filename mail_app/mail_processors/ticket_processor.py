import json
from bs4 import BeautifulSoup

from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.processed_mail import ProcessedMail


class TicketProcessor(AbstractProcessor):

    general_keywords = ["ticket", "boarding pass", "boardingpass"]

    def __init__(self):
        super().__init__()
        self.category = "Ticket"

    def process(self, mail: Mail) -> ProcessedMail:
        if "Your Tickets for" in mail.subject:
            self.__process_eventbrite(mail)
        elif self.__general_conditions(mail):
            return ProcessedMail(self.category, mail.body, mail.time, mail.attachments)
        pass

    def __process_eventbrite(self, mail: Mail) -> ProcessedMail:
        soup = BeautifulSoup(mail.body, 'html.parser')
        schema_script = soup.find('script', type="application/ld+json")
        schema_json = json.loads(schema_script.text)
        processed_mail = ProcessedMail(category="event", description=schema_json['reservationFor']['name'], date=mail.time,
                     attachments=mail.attachments, specifics=schema_json)
        attrs = vars(processed_mail)
        print(', '.join("%s: %s" % item for item in attrs.items()))
        return processed_mail

    ############################################ Conditions ############################################

    def __general_conditions(self, mail: Mail):
        return mail.attachments and \
               (any(keyword in mail.subject.lower() for keyword in self.general_keywords) or
                any(keyword in mail.body.lower() for keyword in self.general_keywords) or
                any(keyword in attachment['name'].lower() for attachment in mail.attachments for keyword in self.general_keywords))

