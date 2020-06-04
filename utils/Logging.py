"""
            get_instance is Static access method for getting object of this logger class.
            This method along with the constructor only allows singleton logger object.
            Partially threadsafe as per requriement to create object orianted framework for Goodreads.
"""

import logging
from decouple import config
import inspect


class Logger:
    __instance = None

    def __init__(self):
        """private constructor."""

        if Logger.__instance != None:
            raise Exception("This class is a singleton, logger object already created.")
        else:
            # handler = logging.StreamHandler()
            # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # handler.setFormatter(formatter)

            logging.basicConfig(filename="newfile.log",
                                format='%(asctime)s - %(processName)s() - %(levelname)s - %(message)s',
                                filemode='w')

            func = inspect.currentframe().f_back.f_code
            # Dump the message + the name of this function to the log.
            # logging.debug("%s: %s in %s:%i" % (
            #     message,
            #     func.co_name,
            #     func.co_filename,
            #     func.co_firstlineno
            # ))

            Logger.__instance = logging.getLogger()  # no name

            Logger.__instance.setLevel(config('LOGLEVEL'))

    @staticmethod
    def get_instance():

        if Logger.__instance == None:
            Logger()
        return Logger.__instance

#
#
#
# """
#             get_instance is Static access method for getting object of this logger class.
#             This method along with the constructor only allows singleton logger object.
#             Partially threadsafe as per requriement to create object orianted framework for Goodreads.
# """
#
# import logging
# from decouple import config
#
#
#
# class Logger:
#     __instance = None
#
#     def __init__(self,name):
#         """private constructor."""
#         self.name = name
#
#         if Logger.__instance != None:
#             raise Exception("This class is a singleton, logger object already created.")
#         else:
#             # handler = logging.StreamHandler()
#             # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#             # handler.setFormatter(formatter)
#
#             logging.basicConfig(filename="newfile.log",
#                                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                                 filemode='w')
#
#             Logger.__instance = logging.getLogger(name=name) #no name
#             Logger.__instance.setLevel(config('LOGLEVEL'))
#
#     @staticmethod
#     def get_instance(name):
#
#         if Logger.__instance == None:
#             Logger(name=name)
#         return Logger.__instance
#
#
# l = Logger.get_instance('name')
#
# l.debug("Harmless debug Message")
# l.info("Just an information")
# l.warning("Its a Warning")
# l.error("Did you try to divide by zero")
# l.critical("Internet is down")
#
#
