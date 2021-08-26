from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        if incoming_msg == 'hello':
            response = "*Hi! I am the Dyneryte Bot*"
            msg.body(response)

        return HttpResponse(str(resp))