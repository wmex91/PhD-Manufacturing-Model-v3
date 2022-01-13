"""
Monitoring.py class:

Class containing the global variables for the model.
"""

import os
import xlwt
# from xlwt import Workbook
from openpyxl import Workbook
from openpyxl import load_workbook
from global_variables import *


class DataLogger(object):
    def __init__(self, path, filename_txt, filename_csv="none"):
        self.path = path

        self.filename_txt = filename_txt
        self.complete_filename_txt = self.path + "\\" + self.filename_txt

        self.filename_csv = filename_csv
        self.heading = self.filename_csv.split("_")[0]
        self.complete_filename_csv = self.path + "\\" + self.filename_csv

        self.initialize_log_txt_file()
        self.initialize_log_csv_file()

    def write_log_txt(self, text):
        with open(self.complete_filename_txt, "a") as f:
            f.write(text)
            f.close()

    def initialize_log_txt_file(self):
        try:
            os.remove(self.complete_filename_txt)
        except FileNotFoundError:
            print("The log file has not been found in the directory, creating a new one.")
            # os.makedirs(self.path)
            with open(self.complete_filename_txt, "w") as f:
                f.close()

    def write_log_csv(self, data_list):
        # csv_log = step, input_level, time_process, output_level, produced, failure, MTTF, MTTR
        text = ''
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                if j+1 == len(data_list[i]):
                    text = text + str(data_list[i][j]) + "\n"
                else:
                    text = text + str(data_list[i][j]) + ", "

        with open(self.complete_filename_csv, "a") as f:
            f.write(text)
            f.close()

    def initialize_log_csv_file(self):
        if self.filename_csv != "none":
            try:
                with open(self.complete_filename_csv, "w") as f:
                    f.close()
            except FileExistsError:
                print('The log file already exists, cleaning up and creating a new one.')
                os.remove(self.complete_filename_csv)
                with open(self.complete_filename_csv, "w") as f:
                    f.close()
            finally:
                # TODO: Maybe instead of time process should be written the number of the processed material ...
                #  or should be added as a column
                with open(self.complete_filename_csv, "a") as f:
                    f.write('step, input ' + self.heading + ', time process ' + self.heading + ', output ' +
                            self.heading + ', produced, failure ' + self.heading + ', MTTF ' + self.heading + ', MTTR ' +
                            self.heading + '\n')
                    f.close()
