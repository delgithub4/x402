class ConfigValidator:

    @staticmethod
    def validate(config):

        if config is None:

            raise ValueError(
                "Configuration missing."
            )

        return True
