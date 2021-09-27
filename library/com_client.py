from files import headers
from files import objects
import client
import requests

sid = None
device = None

class ComClient():
    def __init__(self,comid):
        self.comid = comid
        self.sid = sid
        self.device = device
        self.headers = headers.Headers().headers
        self.headers2 = headers.Headers().headers2
        self.api = "https://service.narvii.com/api/v1"
        self.api2 = "https://aminoapps.com/api"

    # send message
    def send_message(self,chatid: str,msg: str,type: int = 0):
        json1 = {
            "content": msg,
            "type": type
        }
        r = requests.post(f"{self.api}/x{self.comid}/s/chat/thread/{chatid}/message", json=json1, headers=self.headers)
        return r.json

    # join community
    def join_community(self, comid: str):
        json1 = {
            "ndcId": comid
        }
        r = requests.post(f"{self.api2}/join", json=json1, headers=self.headers2)
        return r.json()

    # leave community
    def leave_community(self, comid: str):
        json1 = {
            "ndcId": comid
        }
        r = requests.post(f"{self.api2}/leave", json=json1, headers=self.headers2)
        return r.json()

    # join chat
    def join_chat(self, comid: str, chatid: str):
        json1 = {
            "ndcId": "x"+comid,
            "threadId": chatid
        }
        r = requests.post(f"{self.api2}/join-thread", json=json1, headers=self.headers2)
        return r.json()

    # leave chat
    def leave_chat(self, comid: str, chatid: str):
        json1 = {
            "ndcId": "x"+comid,
            "threadId": chatid
        }
        r = requests.post(f"{self.api2}/leave-thread", json=json1, headers=self.headers2)
        return r.json()

    # follow user
    def follow_user(self, comid: str, user_Id: str):
        json1 = {
            "followee_id": user_Id,
            "ndcId": "x"+comid
        }
        r = requests.post(f"{self.api2}/follow-user", json=json1, headers=self.headers2)
        return r.json()

    # unfollow user
    def unfollow_user(self, comid: str, user_Id: str):
        json1 = {
            "followee_id": user_Id,
            "ndcId": "x"+comid
        }
        r = requests.post(f"{self.api2}/unfollow-user", json=json1, headers=self.headers2)
        return r.json()
