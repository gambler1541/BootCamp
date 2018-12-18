def quick_sort(data, start, end):
    # 탈출 조건
    if start >= end:
        return

    left = start
    right = end
    pivot = data[(start + end) // 2]

    # left와 right가 교차할 때까지 반복
    while left <= right:
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1

        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    quick_sort(data, start, right)
    quick_sort(data, left, end)


if __name__ == '__main__':
    data = [10,3,5,1,7,9,4]
    quick_sort(data, 0, len(data) - 1)
    print(data)

