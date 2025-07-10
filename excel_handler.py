from openpyxl import load_workbook, Workbook
import os
import pandas as pd

class GradeProcessor:

    def __init__(self,input_file):
        self.input_file = input_file
        self.subjects = ["POO", "MOO", "WEB", "THL", "Linux", "LE1", "CAS"]
        self.df = None

    def read_excel(self):
        try:
            self.df = pd.read_excel(self.input_file)
            print("File read successfully")
        except Exception as e:
            print(f"Error while reading file: {e}")

    def calculate_average (self):
        if self.df is not None:
            self.df["Moyenne"] = self.df[self.subjects].mean(axis=1).round(2)
            print ("average calculated successfully")

    def verification(self):
        print("verification...")
        def check_result(moy):
            if moy >= 12:
                return 'V'
            else:
                return 'R'

        if self.df is not None:
            self.df["Résultat"] = self.df["Moyenne"].apply(check_result)

    def process(self):
        self.read_excel()
        self.calculate_average()
        self.verification()
        print(self.df)


if __name__ == "__main__":
    processor = GradeProcessor(input_file="notes.xlsx")
    processor.process()

