"""
Monitoring.py class:

Class containing the global variables for the model.
"""

import os
import xlwt
# from xlwt import Workbook
from openpyxl import Workbook



class DataLogger(object):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.complete_filename = self.path + "\\" + self.filename
        self.initialize_log_file()

    def write_log(self, text):
        with open(self.complete_filename, "a") as f:
            f.write(text)
            f.close()

    def initialize_log_file(self):
        try:
            os.remove(self.complete_filename)
        except FileNotFoundError:
            print("The log file has not been found in the directory, creating a new one.")
            os.makedirs(self.path)
            with open(self.complete_filename, "w") as f:
                f.close()

    def initialize_excel_file(self):
        # Create the workbook
        wb = Workbook()
        # add_sheet is used to create sheet.
        sheet1 = wb.active
        sheet1.title = "Sheet 1"
        # Writing the heading
        sheet1['A1'] = "Timestep [step]"

        sheet1['B1'] = "input A [level]"
        sheet1['C1'] = "timeprocess A [step]"
        sheet1['D1'] = "output A [level]"
        sheet1['E1'] = "failure A [bool]"
        sheet1['F1'] = "MTTF A [step]"
        sheet1['G1'] = "MTTR A [step]"

        sheet1['H1'] = "input B [level]"
        sheet1['J1'] = "timeprocess B [step]"
        sheet1['K1'] = "output B [level]"
        sheet1['L1'] = "failure B [bool]"
        sheet1['M1'] = "MTTF B [step]"
        sheet1['N1'] = "MTTR B [step]"

        sheet1['O1'] = (0, 0, "input C [level]")
        sheet1['P1'] = (0, 0, "timeprocess C [step]")
        sheet1['Q1'] = (0, 0, "output C [level]")
        sheet1['R1'] = (0, 0, "failure C [bool]")
        sheet1['S1'] = (0, 0, "MTTF C [step]")
        sheet1['T1'] = (0, 0, "MTTR C [step]")

        wb.save("C:\\Users\\wmatt\\Desktop\\Workspace\\Projects\\Phd-Projects\\Phd-Manufacturing-Model-v3\\" +
                "empty_workbook.xlsx")
