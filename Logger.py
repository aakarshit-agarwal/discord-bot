import logging
import Configuration

config = Configuration.Configuration()

loggingConfig = config.getLoggingLevel()
switcher = {
    "DEBUG" : logging.DEBUG,
    "INFO" : logging.INFO,
    "WARNING" : logging.WARNING,
    "ERROR" : logging.ERROR,
    "CRITICAL" : logging.CRITICAL,
    "NOTSET" : logging.NOTSET
}

logging.basicConfig(level = switcher[loggingConfig], format = '%(name)s-%(levelname)s-%(message)s')
logger = logging.getLogger()
logger.warning("Logging Started")