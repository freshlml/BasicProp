import logging
import sys

# common logger
common_logger = logging.getLogger("common_logger")
common_logger.setLevel(logging.DEBUG)

__formatter = logging.Formatter(fmt='{asctime} [{levelname}] "{pathname}" at {lineno} lines, [{threadName}]: {message}', datefmt="%Y-%m-%d %H:%M:%S", style="{")

__streamHandler = logging.StreamHandler(sys.stderr)
__streamHandler.setFormatter(__formatter)
__streamHandler.setLevel(logging.DEBUG)
common_logger.addHandler(__streamHandler)

__fileHandler = logging.FileHandler(filename="log_out_common", mode="w", encoding="utf-8")
__fileHandler.setFormatter(__formatter)
__fileHandler.setLevel(logging.DEBUG)
common_logger.addHandler(__fileHandler)






