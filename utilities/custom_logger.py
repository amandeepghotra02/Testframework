import inspect
import logging


# This method will receive log level from the class who needs logging and then handle logging messages
def customLogger(loglevel = logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # by default , log all messages
    logger.setLevel(logging.DEBUG)

# a means append, w means overwriting the previous lgs, we wanna keep previously run logs
# automation.log 1 log file file be created for all test cases/classes
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s' ,
                                  datefmt='%m/%d/%y %I: %M: %S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger