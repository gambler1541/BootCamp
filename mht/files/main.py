from functions import *

if __name__=='__main__':
    raw_data = get_data_from_excel('class_2_3.xlsx')
    scores = list(raw_data.values())
    
    avrg = average(scores)
    variance = variance(scores, avrg)
    standarad_deviation = std_dev(variance)
    
    print('평균: {0}, 분산: {1}, 표준편차: {2}'.format(
    avrg, variance, standarad_deviation))
    evaluateClass(avrg, 50, standarad_deviation, 20)
