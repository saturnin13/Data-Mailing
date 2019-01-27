from multiprocessing import Process

from mail_app.mail import Mail
from mail_app.mail_processors.application_processor import ApplicationProcessor
from mail_app.mail_processors.password_processor import PasswordProcessor
from mail_app.mail_processors.promo_code_processor import PromoCodeProcessor
from mail_app.mail_processors.receipt_processor import ReceiptProcessor
from mail_app.mail_processors.ticket_processor import TicketProcessor


class ProcessorOrchestrator:

    def __init__(self):
        self.application_processor = ApplicationProcessor()
        self.password_processor = PasswordProcessor()
        self.promo_code_processor = PromoCodeProcessor()
        self.receipt_processor = ReceiptProcessor()
        self.ticket_processor = TicketProcessor()

    def process_all_mails(self, mails: [Mail]):
        for mail in mails:
            funs = [self.application_processor.process, self.password_processor.process,
                    self.promo_code_processor.process, self.receipt_processor.process, self.ticket_processor.process]
            processes = [Process(target=process_fn, args=(mail,)) for process_fn in funs]
            for process in processes:
                process.start()
                process.join()
