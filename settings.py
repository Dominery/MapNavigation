class Settings(object):
    def __init__(self):
        self.window_size = (1080, 640)
        self.caption = "MapNavigation"
        self.clock = 30
        self.start_background = "../resources/index.jpg"
        self.start_title = "北斗导航系统"
        self.quit_background = "../resources/final.jpg"
        self.font = {'start': "../resources/李旭科书法.ttf", 'quit': "../resources/李旭科书法.ttf"}


class Request(object):
    _shared_dict = {}

    def __new__(cls, *args, **kwargs):
        instance = super(Request, cls).__new__(cls, *args, **kwargs)
        instance.__dict__ = cls._shared_dict
        return instance

    def __init__(self):
        if not self._shared_dict:
            self._server = []

    def add_server(self, server):
        if server not in self._server:
            self._server.append(server)

    def send(self, request):
        for server in self._server:
            server.receive(request)
