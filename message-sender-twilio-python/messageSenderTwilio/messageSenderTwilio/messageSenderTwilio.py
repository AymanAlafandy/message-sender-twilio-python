from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC977a41a1943f1d902ef22f9ce3f267d9"
# Your Auth Token from twilio.com/console 
auth_token  = "78e99132a43d4cbf299fe6a5e947b06e"

client = Client(account_sid, auth_token) 

messageToOpen =open("C:\Users\AymanAlafandy\Desktop\ooo.txt")# put a path to your file
message = client.messages.create(
    to="+46764279067", #telphone number
    from_="+18313378233", #telephone number 
    body=messageToOpen.read())
    
print(message.sid)
print 32
