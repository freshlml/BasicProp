import logging

# 配置 日志输出目的地，日志输出格式，日志记录级别
# filename: same as open函数file参数; 使用该参数的值创建FileHandler(默认使用StreamHandler which writes to sys.stderr)
# filemode: same as open函数的mode参数，defaults to 'a'，3.9以上版本才能指定encoding，乱码问题
# format: 格式，默认BASIC_FORMAT
# datefmt: 日期格式，与 time.strftime() 支持的格式相同
# style: If a format string is specified, use this to specify the type of format string
#   (possible values '%', '{', '$', for %-formatting, :meth:`str.format` and :class:`string.Template` - defaults to '%')
# level: 日志记录级别, logging.DEBUG，logging.INFO ...

# stream： Use the specified stream to initialize the StreamHandler. is incompatible with 'filename'
#          if both are present, 'stream' is ignored
# handlers: If specified, this should be an iterable of already created
#               handlers, which will be added to the root handler. Any handler
#               in the list which does not have a formatter assigned will be
#               assigned the formatter created in this function
logging.basicConfig(filename="log_out", filemode='w', level=logging.DEBUG,
                    format='{asctime} {levelname} {module} {lineno} {threadName}: {message}',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    style="{",)

logging.debug("1111\n11")
logging.info("%s %s", '22222', 1)
# logging.info("one {0} {1}", 1, 2)  # error: LogRecord#getMessage: "one %d %d" % args; not "one {0} {1}".format(1, 2)
logging.warning("33333")
logging.error("44444")

logging.warning("中文?")  # 乱码，高版本python才能在logging.basicConfig中指定encoding=utf-8(chapter2_9 open(...,encoding=utf-8,...))






