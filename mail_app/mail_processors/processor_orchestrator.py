from mail_app.mail import Mail
from mail_app.mail_processors.application_processor import ApplicationProcessor
from mail_app.mail_processors.password_processor import PasswordProcessor
from mail_app.mail_processors.promo_code_processor import PromoCodeProcessor
from mail_app.mail_processors.ticket_processor import TicketProcessor


class ProcessorOrchestrator:

    def __init__(self):
        self.application_processor = ApplicationProcessor()
        self.password_processor = PasswordProcessor()
        self.promo_code_processor = PromoCodeProcessor()
        self.ticket_processor = TicketProcessor()

    def process_all_mails(self, mails: [Mail]):
        for mail in mails:
            self.application_processor.process(mail)
            self.password_processor.process(mail)
            self.promo_code_processor.process(mail)
            self.ticket_processor.process(mail)
