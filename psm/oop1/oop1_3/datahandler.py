# 데이터를 파일에서 읽어오는 것부터 실제적인 연산, 평가, 결과 출력까지 잠당 하는 클래스
# 1. 객체가 생성되는 순간 생성자 함수에서 모든 연산을 마치고 그 결과 값을 인스턴스 멤버에 저장해 두는 경우 ( 클래스가 확장되면 연산 횟수가 늘어서 비합리적)
# 2. 데이터가 필요할 때마다 매번 연산하는 경우( 연산을 반복하는것은 매우 비효율적 )
# 3. 프로그래머가 데이터를 요청할 때 한 번도 연산된 적이 없다면 필요한 만큰만 연산하여 결과 값을 저장해 두는 경우

from statistics import *
import openpyxl


class DataHandler:
    # 클래스 멤버 evaluator 에 Stat 객체를 할당,
    # Stat 객체의 평균, 분산, 표준편차 연산 함수는 모든 객체가 공유해서 사용
    evaluator = Stat()
    @classmethod
    # 엑셀 파일에서 데이터를 읽어오는 함수를 클래스 메서드로 만듬
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        return dic

    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.your_class = year_class
        # 연산한 값을 저장해 두는 저장소
        # 필요할 때 연산하되
        # 이미 연산된 값이면 연산 없이 저장된 값을 반환

        # 객체에 연산 결과를 저장해 둘 캐시로 딕셔너리를 사용
        self.cache = {}

    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())

        return self.cache.get('scores')

    # 평균을 반환하는 메서드
    def get_average(self):
        # varage 라는 키가 있는지 확인, 없으면 평균이 구해지지 않은 상태이므로 클래스 멤버인 evaluator로 평균을 구하고 캐시에 저장
        if 'verage' not in self.cache:
            self.cache['average'] = self.evaluator.average(self.get_scores())

        # 키가 있다면 이미 연산 결과가 저장된 상태이므로 캐시에 저장된 값을 반환
        return self.cache.get('average')

    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(self.get_scores(), self.get_average())

        return self.cache.get('variance')

    # 객체를 생성한다음 처음으로 표준편차를 반환하는 메서드를 호출한다면 if문으로 키의 유무를 검사
    # 키가 없다면 각 메서드에서 차례대로 호출해 연산 결과를 차곡차곡 캐시에 쌓은 다음에 값을 반환, 필요한 시점에 필요한 연산만 하는 셈
    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation'] = self.evaluator.std_dev(self.get_variance())

        return self.cache.get('standard_deviation')

    # 평균, 전체 평균, 표준편차를 이용해 학급의 성적을 평가
    def evaluate_calss(self, total_avrg, sd):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()

        if avrg < total_avrg and std_dev > sd:
            print('성적이 너무 저조하고 학생들의 실력 차이가 너무크다.')
        elif avrg > total_avrg and std_dev > sd:
            print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
        elif avrg < total_avrg and std_dev < sd:
            print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
        elif avrg > total_avrg and std_dev < sd:
            print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')

    # 최종적으로 학급의 평균, 분산, 표준편차, 종합평가를 출력
    def get_evaluation(self, total_avrg, sd = 20):
        print('*' * 50)
        print('{} 반 성적 분석 결과'.format(self.your_class))
        print('{0}반의 평균은 {1}점이고 분산은 {2}이며 따라서 표준편차는 {3}이다.'.format(self.your_class, self.get_average(), self.get_variance(), self.get_standard_deviation()))
        print('*' * 50)
        print('{} 반 종합 평가'.format(self.your_class))
        print('*' * 50)
        self.evaluate_calss(total_avrg, sd)


if __name__ == '__main__':
    DataHandler