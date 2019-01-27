import base64
import re
from datetime import datetime

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import httplib2
from googleapiclient.discovery import build
from oauth2client.client import AccessTokenCredentials

from mail_app.mail import Mail
from mail_app.mail_postprocessor.postprocessor import PostProcessor
from mail_app.mail_processors.processor_orchestrator import ProcessorOrchestrator


class Index(TemplateView):
    template_name = "index.html"


class UserView(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        token = request.POST['token']

        credentials = AccessTokenCredentials(token, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build('gmail', 'v1', http=http)

        # Call the Gmail API
        mails = []
        USER_ID = 'me'
        results = service.users().messages().list(userId=USER_ID).execute()

        for i, m in enumerate(results['messages'][0:10]):
            print('MESSAGE #%d\n' % i)
            # message = service.users().messages().get(userId=USER_ID, id=m['id'], format='raw').execute()

            message_full = service \
                .users() \
                .messages() \
                .get(userId=USER_ID, id=m['id'], format='full') \
                .execute() \
                .get('payload', {})
            msg_headers = message_full.get('headers', [])

            #
            # Header
            #

            required_headers = ['From', 'Subject', 'Date']

            headers = {}
            for header in msg_headers:
                name, value = header['name'], header['value']
                if name in required_headers:
                    headers[name] = value

            print('headers: ', headers)

            #
            # Attachments
            #

            def parse_content(content, body_, attachments_):
                msg_body = content.get('body', {})
                msg_parts = content.get('parts', [])

                if msg_body == {} and msg_parts == []:
                    return body_, attachments_

                # Is attachment?
                att_id = msg_body.get('attachmentId')
                if att_id:
                    att = service \
                        .users() \
                        .messages() \
                        .attachments() \
                        .get(userId=USER_ID, messageId=m['id'], id=att_id) \
                        .execute()
                    attachments_[content['filename']] = base64.urlsafe_b64decode(att['data'])

                # Is text?
                text = msg_body.get('data')
                if text:
                    body_ += str(base64.urlsafe_b64decode(text))

                for part in msg_parts:
                    b, c = parse_content(part, body_, attachments_)
                    body_ += b
                    attachments_.update(c)
                return body_, attachments_

            body, attachments = parse_content(message_full, "", {})

            mails.append(
                Mail(token, m['id'], headers['From'], headers['Subject'], body, attachments, headers['Date'])
            )

        # Process all mails and output them to db
        ProcessorOrchestrator().process_all_mails(mails)

        return HttpResponse('Gut !')


def find_regex(regex, body):
    search_result = re.compile(regex, 0).search(body)

    if not search_result:
        return None

    return search_result.groups()[0]