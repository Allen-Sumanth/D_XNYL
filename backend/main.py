import secrets
from urllib import response
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
import httpx
import firebase_admin
from firebase_admin import credentials, messaging

app = FastAPI()
firebase_cred = credentials.Certificate("firebase.json")
firebase_app = firebase_admin.initialize_app(firebase_cred)

topic = "notifs"
def subsribe_notifs(tokens):
    response = messaging.subscribe_to_topic(tokens, topic)
    if response.failure_count > 0:
        print(f"Failed to subscribe to topic {topic} due to {list(map(lambda e: e.reason,response.errors))}")

def send_notification(title, body):
    message = messaging.Message(
        notification = messaging.Notification(
            title = title,
            body = body
        ),
        topic = topic
    )
    messaging.send(message=message)

message = messaging.Notification(
    title = "notif",
    body="hi"
)

dauth_client_id =  "6cEtBzO42pTHXuNC"
dauth_client_secret = "aAL1vX7rp8lkfVt6sS4x4ked6vCu9rIU"
callback_uri = "http://localhost:8000/gettoken"
client_state = secrets.token_urlsafe()
nonce = secrets.token_urlsafe()

@app.get("/dauth-login")
async def dauth_login():
    return RedirectResponse(f"https://auth.delta.nitt.edu/authorize?client_id={dauth_client_id}&redirect_uri={callback_uri}&response_type=code&grant_type=authorization_code&state={client_state}&scope=user&nonce={nonce}")

@app.get("/gettoken")
async def gettoken(code: str, state: str):
    # return {"message":"oho"}
    if(state != client_state):
        return {"message":"auth failed"}
    else:
        async with httpx.AsyncClient() as client:
            params = {
                'client_id':dauth_client_id,
                'client_secret':dauth_client_secret,
                'grant_type':'authorization_code',
                'code':code,
                'redirect_uri':callback_uri
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            print(dauth_client_id)

            response = await client.post(url = f"https://auth.delta.nitt.edu/api/oauth/token?client_id={dauth_client_id}&client_secret={dauth_client_secret}&grant_type=authorization_code&code={code}&redirect_uri={callback_uri}", headers=headers)
            response_json = response.json()
            return response_json
        
def send_push_notification(token, title, body):
    # Create a message to send to the device
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    # Send the message
    response = messaging.send(message)
    print('Successfully sent message:', response)

@app.get("/notif")
async def send_notification(title: str, body: str):
    
    device_token = 'fbUZnNp8SRy6DIPvFsST5v:APA91bF_WrX-Bx5eCc745XQz1J7lWaP05QLVHgu_tCOvP6W69X7no-Se7zhykBhjFVOh_MIIturMeYRIice-a650hdOVimAEG9O0tADiT2U_UXYMLOEWEOgR4MEVn-PfsCqf3VREz_5R'
    notification_title = 'Hello'   
    notification_body = 'This is a push notification'
    send_push_notification(device_token, notification_title, notification_body)
