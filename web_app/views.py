import base64

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import httplib2
from googleapiclient.discovery import build
from oauth2client.client import AccessTokenCredentials


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

        for m in results['messages'][:1]:
            message = service.users().messages().get(userId='me', id=m['id'], format='raw').execute()
            print('Message snippet: %s' % message['snippet'])

            msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
            # mime_msg = email.message_from_string(msg_str)

            print(str(msg_str))

        return HttpResponse(token)
