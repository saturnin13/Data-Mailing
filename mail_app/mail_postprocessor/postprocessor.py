from mail_app.processed_mail import ProcessedMail


class PostProcessor:
    def post_process(self, mail: ProcessedMail):
        insert_processed_email(user_id=mail.user_id, date=mail.date, from_=mail.from_, description=mail.description,
                               attachements=mail.attachments, category=mail.category)
        pass
