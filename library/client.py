from files import headers
from files import objects
import com_client

import requests
class Client():

    def __init__(self,sid: str,deviceid=None):
        headers.device = deviceid
        headers.sid = sid
        com_client.device = deviceid
        com_client.sid = sid
        self.api = "https://service.narvii.com/api/v1"
        self.api2 = "https://aminoapps.com/api"

