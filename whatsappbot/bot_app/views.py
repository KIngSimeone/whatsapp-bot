from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
import twilio

def index(request):
    print(twilio)
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        if incoming_msg == 'hello':
            response = "*Hi! Welcome to dyneryte* To get started kindly type in your phone number"
            msg.body(response)
            phone = request.POST['Body'].lower()
            print(phone)     

        return HttpResponse(str(resp))