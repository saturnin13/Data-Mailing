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

        results = service.users().messages().list(userId='me').execute()

        mails = []

        for m in results['messages']:
            message = service.users().messages().get(userId='me', id=m['id'], format='raw').execute()

            msg_str = str(base64.urlsafe_b64decode(message['raw'].encode('UTF-8')))

            time = datetime.fromtimestamp(int(message['internalDate']) / 1000)
            user_id = token
            from_ = find_regex("smtp.mailfrom=(.*?)\\\\r", msg_str).replace(';', '')
            subject = find_regex("Subject: (.*?)\\\\r", msg_str)
            body = msg_str
            attachments = {}

            mails.append(
                Mail(user_id, from_, subject, body, attachments, time)
            )

        # Process all mails and output them to db
        ProcessorOrchestrator().process_all_mails(mails)

        return HttpResponse('Gut !')


def find_regex(regex, body):
    search_result = re.compile(regex, 0).search(body)

    if not search_result:
        return None

    return search_result.groups()[0]