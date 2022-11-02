import sys
import os
import logging
# .../Python37/Lib/logging/__init__.py API

# LogRecord, A LogRecord instance represents an event being logged
# LogRecord#getMessage: '...' % args，not "one {0} {1}".format(1, 2)
logRecord = logging.LogRecord("one-name", logging.WARNING, "", 0, "one %d %d", (1, 2), None)
print(logRecord.getMessage())  # one 1 2


# Style, Formatter Style, StrFormatStyle for example
logRecord.__dict__['message'] = logRecord.getMessage()
strFormatStyle = logging.StrFormatStyle("{levelname}:{name}:{message}")
print(strFormatStyle.format(logRecord))  # WARNING:one-name:one 1 2

# Formatter, LogRecord convert to Text
formatter = logging.Formatter(fmt="{levelname}:{name}:{message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
print(formatter.format(logRecord))  # WARNING:one-name:one 1 2


# Filter, Loggers and Handlers can optionally use Filter instances to filter records as desired


# Handler, Handler instances dispatch logging events to specific destinations
# 1. StreamHandler: A handler class which writes logging records, appropriately formatted,
#                   to a stream. Note that this class does not close the stream
formatter2 = logging.Formatter(fmt="{levelname}:{name}:{message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setFormatter(formatter2)
streamHandler.setLevel(logging.DEBUG)
logRecord2 = logging.LogRecord("two-name", logging.WARNING, "", 0, "two %d %d", (1, 2), None)
streamHandler.emit(logRecord2)  # WARNING:two-name:two 1 2

# 2. FileHandler: A handler class which writes formatted logging records to disk files.
#                 close method close the file
fileHandler = logging.FileHandler(filename="log_out", mode="w", encoding="utf-8")
formatter3 = logging.Formatter(fmt="{levelname}:{name}:{message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
fileHandler.setFormatter(formatter3)
fileHandler.setLevel(logging.DEBUG)
logRecord3 = logging.LogRecord("three-name", logging.WARNING, "", 0, "three中 %d %d", (1, 2), None)
try:
    fileHandler.emit(logRecord3)
finally:
    fileHandler.close()


# Logger, Instances of the Logger class represent a single logging channel. A
#     "logging channel" indicates an area of an application. Exactly how an
#     "area" is defined is up to the application developer. Since an
#     application can have any number of areas, logging channels are identified by a unique string
logger = logging.getLogger("chapter7_36")
logger.setLevel(logging.INFO)

formatter4 = logging.Formatter(fmt="{asctime} {levelname} {module} {lineno} {threadName}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")

streamHandler2 = logging.StreamHandler(sys.stderr)
streamHandler2.setFormatter(formatter4)
streamHandler2.setLevel(logging.DEBUG)
logger.addHandler(streamHandler2)

fileHandler2 = logging.FileHandler(filename="log_out", mode="w", encoding="utf-8")
fileHandler2.setFormatter(formatter4)
fileHandler2.setLevel(logging.DEBUG)
logger.addHandler(fileHandler2)

logger.debug("1111\n11")
logger.info("%s %s", '22222', 1)
logger.warning("33333-中")
logger.error("44444")

# logging.shutdown()  # first: logging的shutdown
# os.remove("log_out")  # then: delete file



