import logging

logger = logging.getLogger('simpleExample')  # with same name


def md():
    logger.debug("chapter7_37_1运行")


if __name__ == "__main__":
    logger.warning("单独运行")

