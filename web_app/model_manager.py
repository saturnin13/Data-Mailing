import hashlib
import os
import pickle

import dateparser

from .models import ProcessedEmail


def get_attachments_dir():
    curr_dir = os.path.dirname(__file__)
    att_dir = os.path.realpath(os.path.join(curr_dir, '../static/attachments'))
    os.makedirs(att_dir, exist_ok=True)
    return att_dir


def insert_processed_email(user_id, message_id, date, from_, description, attachments, category):
    att_dump = pickle.dumps(attachments)
    attachment_hash = hashlib.md5(att_dump).hexdigest()
    filename = "{}.pickle".format(attachment_hash)
    attachment_location = os.path.join(get_attachments_dir(), filename)

    if not os.path.exists(attachment_location):
        with open(attachment_location, "wb") as fd:
            fd.write(att_dump)

    ProcessedEmail.objects.update_or_create(
        message_id=message_id,
        category=category,
        defaults=dict(
            message_id=message_id,
            category=category,
            user_id=user_id,
            date=dateparser.parse(date[:-6]),
            sender=from_,
            description=description,
            attachment_location=attachment_location,
        )
    )


def get_processed_emails(user_id):
    emails = ProcessedEmail.objects.get(user_id=user_id)
    if emails is None:
        return None

    full_emails = []
    for email in emails:
        with open(email.attachment_location, "rb") as fd:
            attachments = pickle.load(fd)
            full_emails.append(dict(
                user_id=email.user_id,
                message_id=email.message_id,
                date=email.date,
                from_=email.sender,
                description=email.description,
                attachments=attachments,
                category=email.category
            ))

