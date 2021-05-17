# 6-1
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def solve(num_list):
    result = 0
    for num in num_list:
        result += num
    return result


def solve2(num):
    return sum(num)
