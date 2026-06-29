from providers.provider_factory import ProviderFactory


class ConfigManager:

    def __init__(self):

        self.provider = ProviderFactory.config()

    def get(
        self,
        key,
        default=None,
    ):

        return self.provider.get(
            key,
            default,
        )
