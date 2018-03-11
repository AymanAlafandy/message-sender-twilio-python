from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""# get it from twilio
# Your Auth Token from twilio.com/console 
auth_token  = ""# get it from twilio

client = Client(account_sid, auth_token) 

messageToOpen =open("C:\Users\AymanAlafandy\Desktop\ooo.txt")# put a path to your file
message = client.messages.create(
    to="+46764279067", #telphone number
    from_="+18313378233", #telephone number 
    body=messageToOpen.read())
    
print(message.sid)
print 32
