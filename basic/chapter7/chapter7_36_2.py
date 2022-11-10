import logging
import sys


logger = logging.getLogger("chapter7_36_simple_name")
logger.setLevel(logging.INFO)
print("chapter7_36_2: ", logger)

formatter = logging.Formatter(fmt="{asctime} {levelname} {module} {lineno} {threadName}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
print("chapter7_36_2: ", formatter)

streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)
print("chapter7_36_2: ", streamHandler)
logger.addHandler(streamHandler)

fileHandler = logging.FileHandler(filename="log_out_1", mode="w", encoding="utf-8")
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
print("chapter7_36_2: ", fileHandler)
logger.addHandler(fileHandler)


print("----------")




