class EndpointManager:

    def __init__(self):

        self.routes = []

    def register(self, route):

        self.routes.append(route)

    def all(self):

        return self.routes
