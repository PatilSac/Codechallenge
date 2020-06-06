import json
import os
from utils import output_process


class Startup():

    @staticmethod
    def initialize():
        output_process.OP.process_output()

