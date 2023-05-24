# Made by tq148 (rblxdeve) don't say you made this code bruv.
import requests

target_id = 00000
cookie = ""
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

userid= requests.get('https://www.roblox.com/my/settings/json', headers=headers).json()['UserId']

data = {
    "userId": userid, # your user id
    "subject": "boss man",
    "body": "you've been struck by tq148",
    "recipientId": target_id # recipient's user Id
}
import time, os
while True:
    message_response = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers = headers, data = data)
    print(f'{message_response.json()},{message_response.status_code}")   
    if message_response.status_code == 429:
        time.sleep(60)
    if message_response.status_code ==403:
        os.system('python 9000RTE.py')
    time.sleep(5)
