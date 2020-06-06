"""
            get_instance is Static access method for getting object of this logger class.
            This method along with the constructor only allows singleton logger object.
            Partially threadsafe as per requriement to create object orianted framework for Goodreads.
"""

import logging
import os
from datetime import datetime

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

            FILENAME = os.path.dirname(os.getcwd())+"/logs"
            datetimecomp = datetime.now().strftime('_%d_%m_%Y__%H:%M')

            logging.basicConfig(filename=FILENAME+ "/log" + str(datetimecomp) + ".log",
                                format='%(asctime)s - %(module)s -%(funcName)s - %(lineno)s - %(levelname)s - %(message)s',
                                filemode='w',


                                )

            # func = inspect.currentframe().f_back.f_code

            Logger.__instance = logging.getLogger()  # no name
            Logger.__instance.setLevel(config('LOGLEVEL'))

    @staticmethod
    def get_instance():

        if Logger.__instance == None:
            Logger()
        return Logger.__instance
