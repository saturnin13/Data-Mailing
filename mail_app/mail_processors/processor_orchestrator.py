from concurrent.futures import ThreadPoolExecutor

from mail_app.mail import Mail
from mail_app.mail_postprocessor.postprocessor import PostProcessor
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
        self.postprocessor = PostProcessor()

    def process_and_insert(self, processing_fn, mail: Mail):
        self.postprocessor.post_process(processing_fn(mail))

    def process_all_mails(self, mails: [Mail]):
        for fun in [self.application_processor.process, self.password_processor.process,
                    self.promo_code_processor.process, self.receipt_processor.process, self.ticket_processor.process]:
            with ThreadPoolExecutor(max_workers=50) as executor:
                executor.map(lambda data: self.process_and_insert(fun, mails), mails)

    def process_no_parallel(self, mails):
        for mail in mails:
            for fun in [self.application_processor.process, self.password_processor.process,
                        self.promo_code_processor.process, self.receipt_processor.process,
                        self.ticket_processor.process]:
                self.process_and_insert(fun, mail)
