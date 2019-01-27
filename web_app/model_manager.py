import hashlib
import os
import pickle

from .models import ProcessedEmail


def get_attachments_dir():
    curr_dir = os.path.dirname(__file__)
    att_dir = os.path.realpath(os.path.join(curr_dir, '../static/attachments'))
    os.makedirs(att_dir, exist_ok=True)
    return att_dir


def insert_processed_email(user_id, date, from_, description, attachments, category):
    att_dump = pickle.dumps(attachments)
    attachment_hash = hashlib.md5(att_dump).hexdigest()
    filename = "{}.pickle".format(attachment_hash)
    attachment_location = os.path.join(get_attachments_dir(), filename)
    print("Storing attachment at path " + attachment_location)

    if not os.path.exists(attachment_location):
        with open(attachment_location, "wb") as fd:
            fd.write(att_dump)

    ProcessedEmail.objects.update_or_create(
        user_id=user_id,
        defaults=dict(
            user_id=user_id, date=date, sender=from_, description=description,
            attachment_location=attachment_location, category=category
        )
    )


def get_processed_email(user_id):
    email = ProcessedEmail.objects.get(pk=user_id)
    if email is None:
        return None

    with open(email.attachment_location, "rb") as fd:
        attachments = pickle.load(fd)

    return dict(
        user_id=email.user_id,
        date=email.date,
        from_=email.sender,
        description=email.description,
        attachments=attachments,
        category=email.category
    )

