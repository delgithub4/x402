from abc import ABC, abstractmethod


class HealthInterface(ABC):

    @abstractmethod
    def check(self):
        ...
