from openpyxl import load_workbook, Workbook
import os
import pandas as pd

class ExcelHandler:

    @staticmethod
    def read_excel(file_path):

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")

        return pd.read_excel(file_path)


