import openpyxl
import math

def get_data_from_excel(filename):
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows
    
    for name, score in g:
        dic[name.value] = score.value
        
    return dic

def average(scores):
    s = 0
    for score in scores:
        s += score
    return round(s/len(scores), 1)

def variance(scores, avrg):
    s = 0
    for score in scores:
        s += (score - avrg) ** 2
    return round(s/len(scores), 1)

def std_dev(variance):
    return round(math.sqrt(variance), 1)

def evaluateClass(avrg, total_avrg, std_dev, sd):
    if avrg < total_avrg and std_dev > sd:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avrg > total_avrg and std_dev > sd:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avrg < total_avrg and std_dev < sd:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avrg > total_avrg and std_dev < sd:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')

