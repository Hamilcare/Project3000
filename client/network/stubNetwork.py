class NetworkStub:
    def __init__(self):
        pass
        
    def request_move(self,movement):
        return True

    def request_map(self):
        new_map = "0 0 800 10 !0 0 10 600 !0 590 800 10 !790 0 10 600"
        return new_map
