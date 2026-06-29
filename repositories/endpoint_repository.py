class EndpointRepository:

    def __init__(self):

        self.endpoints = []

    def save(self, endpoint):

        self.endpoints.append(endpoint)

    def all(self):

        return self.endpoints
