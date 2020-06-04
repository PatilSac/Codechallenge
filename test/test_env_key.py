from utils import logging
import os
"""
First test sample
"""



l = logging.Logger.get_instance()

l.debug("Harmless debug Message")
l.info("Just an information")
l.warning("Its a Warning")
l.error("Did you try to divide by zero")
l.critical("Internet is down")


print(os.path.dirname(os.getcwd()))

