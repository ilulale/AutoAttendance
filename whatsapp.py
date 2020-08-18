from twilio.rest import Client
import os
def sendmsg(msg):

    os.environ["TWILIO_ACCOUNT_SID"] = "AC8364d509b628b6b76ccb1205716f60ef"
    os.environ["TWILIO_AUTH_TOKEN"] = "cd272d7049ddbd7315c7371a7ab65da9"
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client()

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+1 415 523 8886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+919158639011'

    client.messages.create(body=msg,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)
