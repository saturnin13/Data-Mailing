from mail_app.mail import Mail
from mail_app.mail_processors.abstract_processor import AbstractProcessor
from mail_app.mail_processors.processed_mail import ProcessedMail


class TicketProcessor(metaclass=AbstractProcessor):
    def process(self, mail: Mail) -> ProcessedMail:
        keywords = ["ticket", "boarding pass"]
        if mail.from_ == "orders@eventbrite.com":
            self.process_eventbrite(mail)
        elif any(keyword in mail.subject.lower() for keyword in keywords):
            return ProcessedMail(category="ticket", )
        pass

    def process_eventbrite(self, mail: Mail) -> ProcessedMail:
        pass