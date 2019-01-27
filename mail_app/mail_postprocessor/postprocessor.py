from mail_app.processed_mail import ProcessedMail
from web_app.model_manager import insert_processed_email

from bs4 import BeautifulSoup

class PostProcessor:

    def post_process_all(self, mails: [ProcessedMail]):
        for m in mails:
            self.post_process(m)

    def post_process(self, mail: ProcessedMail):
        if mail:
            soup = BeautifulSoup(mail.description, 'html.parser')
            html = soup.html
            description = html or mail.description
            insert_processed_email(user_id=mail.user_id, message_id=mail.message_id,
                                   date=mail.date, from_=mail.from_, description=description,
                                   attachments=mail.attachments, category=mail.category, subject=mail.subject)
