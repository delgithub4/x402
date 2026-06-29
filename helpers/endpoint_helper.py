class EndpointHelper:

    @staticmethod
    def normalize(path):

        return "/" + path.strip("/")
