from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console 
auth_token  = ""

client = Client(account_sid, auth_token) 

message = client.messages.create(
    to="+00000000", #telphone number
    from_="+18313378233", #telephone number 
    body="Du har en fin mobil. Kan jag låna den?")

print(message.sid)
print 32
