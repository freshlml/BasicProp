import logging
import sys
import chapter7_36_2


logger = logging.getLogger("chapter7_36_simple_name")
logger.setLevel(logging.INFO)
print("chapter7_36_1: ", logger)
print("logger same? ", chapter7_36_2.logger is logger)  # True
print(logging.Logger.manager.loggerDict)  # {'chapter7_36_simple_name': <Logger chapter7_36_simple_name (INFO)>}

formatter = logging.Formatter(fmt="{asctime} {levelname} {module} {lineno} {threadName}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
print("chapter7_36_1: ", formatter)
print("formatter same? ", chapter7_36_2.formatter is formatter)  # False

streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)
print("chapter7_36_1: ", streamHandler)
print("streamHandler same? ", chapter7_36_2.streamHandler is streamHandler)  # False
logger.addHandler(streamHandler)

fileHandler = logging.FileHandler(filename="log_out_1", mode="w", encoding="utf-8")
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
print("chapter7_36_1: ", fileHandler)
print("fileHandler same? ", chapter7_36_2.fileHandler is fileHandler)  # False
logger.addHandler(fileHandler)

print(logger.handlers)  # size is 4
print(logging._handlerList)  # 包含logger.handlers




