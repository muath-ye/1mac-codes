from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACaa85b8f2ee82d5b914fab5b014d8bb7d"
# Your Auth Token from twilio.com/console
auth_token  = "5b4c92905db3fce2da5930ab60759f2f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+967777013441", 
    from_="+967733475101",
    body="Hello from Muath!")

print(message.sid)
