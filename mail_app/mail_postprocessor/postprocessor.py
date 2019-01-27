from mail_app.processed_mail import ProcessedMail
from web_app.model_manager import insert_processed_email


class PostProcessor:

    def post_process_all(self, mails: [ProcessedMail]):
        for m in mails:
            self.post_process(m)

    def post_process(self, mail: ProcessedMail):
        if mail:
            insert_processed_email(user_id=mail.user_id, message_id=mail.message_id,
                                   date=mail.date, from_=mail.from_, description=mail.description,
                                   attachments=mail.attachments, category=mail.category)
