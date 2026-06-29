from providers.config_provider import ConfigProvider
from providers.database_provider import DatabaseProvider
from providers.dependency_provider import DependencyProvider
from providers.response_provider import ResponseProvider


class ProviderFactory:

    _instances = {}

    @classmethod
    def database(cls):

        if "database" not in cls._instances:
            cls._instances["database"] = DatabaseProvider()

        return cls._instances["database"]

    @classmethod
    def config(cls):

        if "config" not in cls._instances:
            cls._instances["config"] = ConfigProvider()

        return cls._instances["config"]

    @classmethod
    def responses(cls):

        if "responses" not in cls._instances:
            cls._instances["responses"] = ResponseProvider()

        return cls._instances["responses"]

    @classmethod
    def dependencies(cls):

        if "dependencies" not in cls._instances:
            cls._instances["dependencies"] = DependencyProvider()

        return cls._instances["dependencies"]
