def binary_search(data, target):
    # 전달받은 data를 정렬
    data.sort()
    #start는 시작 인덱스, end는 마지막 인덱스
    start = 0
    end = len(data) - 1

    # start와 end가 교차하기전까지 반복
    while start <= end:
        # mid는 start와 end의 가운데 인덱스
        mid = (start + end) // 2

        # target 데이터가 mid의 데이터와 같다면
        # mid 반환
        if target == data[mid]:
            return mid
        # target이 작다면
        # end를 mid-1로 지정
        elif target < data[mid]:
            end = mid - 1
        # target이 크면
        # start를 mid + 1로 지정
        else:
            start = mid + 1

    # start와 end가 교차했을 때까지
    # target을 찾지 못했다면
    # target이 리스트에 존재하지 않음
    return None


if __name__ == '__main__':
    data = [i ** 2 for i in range(1, 11)]
    target = 23
    idx = binary_search(data, target)

    if idx == None:
        print(f'{target}은/는 존재하지 않습니다')
    else:
        print(f'찾는 데이터의 인덱스는 {idx}이고 데이터는 {data[idx]}입니다.')
