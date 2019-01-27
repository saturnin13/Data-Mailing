import hashlib
import os
import pickle

import dateparser
import pytz

from .models import ProcessedEmail

ATTACHMENTS = 'static/attachments'


def get_attachments_dir():
    curr_dir = os.path.dirname(__file__)
    att_dir = os.path.realpath(os.path.join(curr_dir, '..', ATTACHMENTS))
    return att_dir


def insert_processed_email(user_id, message_id, date, from_, description, attachments, category, subject):
    attachment_hash = hashlib.md5(pickle.dumps(attachments)).hexdigest()
    attachment_location = os.path.join(get_attachments_dir(), attachment_hash)
    os.makedirs(attachment_location, exist_ok=True)

    for filename, data in attachments.items():
        filepath = os.path.join(attachment_location, filename)
        if not os.path.exists(filepath):
            with open(filepath, "wb") as fd:
                fd.write(data)

    ProcessedEmail.objects.update_or_create(
        message_id=message_id,
        category=category,
        defaults=dict(
            message_id=message_id,
            category=category,
            user_id=user_id,
            date=dateparser.parse(date[:-6]).replace(tzinfo=pytz.UTC),
            sender=from_,
            description=description,
            attachment_location=attachment_hash,
            subject=subject
        )
    )


def get_processed_emails(user_id):
    emails = ProcessedEmail.objects.filter(user_id=user_id)
    if emails is None:
        return None

    full_emails = []
    for email in emails:
        attachments = []
        attachment_hash = email.attachment_location
        for filename in os.listdir(os.path.join(get_attachments_dir(), attachment_hash)):
            attachments.append({
                'name': filename,
                'body': os.path.join(ATTACHMENTS, attachment_hash, filename),
            })

        full_emails.append(dict(
            user_id=email.user_id,
            message_id=email.message_id,
            date=str(email.date),
            from_=email.sender,
            description=email.description,
            attachments=attachments,
            category=email.category,
            subject=email.subject
        ))

    final_emails = {
        'Application': [],
        'Password': [],
        'Promo code': [],
        'Receipts': [],
        'Ticket': [],
    }
    for e in full_emails:
        final_emails[e['category']] += [e]

    return [
        {'name': k, 'mails': v} for k, v in final_emails.items()
    ]
