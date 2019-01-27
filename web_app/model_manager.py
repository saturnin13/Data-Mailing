import os
import pickle

from .models import ProcessedEmail


def get_attachments_dir():
    curr_dir = os.path.dirname(__file__)
    att_dir = os.path.realpath(os.path.join(curr_dir, '../static/attachments'))
    os.makedirs(att_dir, exist_ok=True)
    return att_dir


def insert_processed_email(user_id, date, from_, description, attachments,
                           category):
    attachment_hash = str(hash(repr(attachments)))
    filename = "{}.pickle".format(attachment_hash)
    attachment_location = os.path.join(get_attachments_dir(), filename)

    pickle.dump(attachments, attachment_location)

    ProcessedEmail.objects.update_or_create(
        user_id=user_id, date=date, from_=from_, description=description,
        attachment_location=attachment_location, category=category
    )


def get_processed_email(user_id):
    email = ProcessedEmail.objects.get(pk=user_id)
    if email is None:
        return None

    attachments = pickle.load(email.attachment_location)
    return dict(
        user_id=email.user_id,
        date=email.date,
        from_=email.date,
        description=email.description,
        attachments=attachments,
        category=email.category
    )

