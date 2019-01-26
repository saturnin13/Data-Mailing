from bs4 import BeautifulSoup

from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.processed_mail import ProcessedMail


class TicketProcessor(AbstractProcessor):
    def process(self, mail: Mail) -> ProcessedMail:
        keywords = ["ticket", "boarding pass"]
        if "Your Tickets for" in mail.subject:
            self.process_eventbrite(mail)
        elif any(keyword in mail.subject.lower() for keyword in keywords):
            return ProcessedMail(category="ticket", )
        pass

    def process_eventbrite(self, mail: Mail) -> ProcessedMail:
        soup = BeautifulSoup(mail.body, 'html.parser')
        schema_script = soup.find(type="application/ld+json")
        print(schema_script)
