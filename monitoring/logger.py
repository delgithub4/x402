from core.logging_config import logger


class ApplicationLogger:

    def info(self, message):

        logger.info(message)

    def warning(self, message):

        logger.warning(message)

    def error(self, message):

        logger.error(message)
