import logging

logger = logging.getLogger('simpleExample.sub')  # with sub name


def md():
    logger.debug("sub运行")


if __name__ == "__main__":
    logger.warning("单独运行")



