from statistics import *
import openpyxl

class DataHandler:
    evaluator = Stat()
    
    @classmethod
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows
    
        for name, score in g:
            dic[name, value] = score.value
        
        return dict

def __init__(self, filename, year_class):
    self.filename = filename
    self.year_class = 

    self.cache = {}
