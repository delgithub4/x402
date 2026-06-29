class RouterManager:

    def __init__(self):

        self.routers = []

    def include(self, router):

        self.routers.append(router)

    def registered(self):

        return self.routers
