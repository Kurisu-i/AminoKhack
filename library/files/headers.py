sid = None
device = None

class Headers:
    def __init__(self):
        self.headers = {
            "NDCAUTH": sid,
            "NDCDEVICEID": device
        }
        if device==None:
            self.headers["NDCDEVICEID"] = "228141909FD3D79BA1C68CD99AE8A3024C6EB2E30DAC81534B7C1B1D50F44DD6D71243164B52F5671A"

        self.headers2 = {
        	"cookie": sid,
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
            "x-requested-with": "xmlhttprequest"
        }
