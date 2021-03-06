# 1-1
# Hello World!를 출력하시오.

print("Hello World!")
print('*' * 100)


# 1-2
# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

army = "강한친구 대한육군"
print(army + '\n' + army)
print('*' * 100)


# 1-3
# 고양이를 출력한다.

print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
print('*' * 100)


# 1-4
# 개를 출력한다.

print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|')
print('*' * 100)


# 1-5
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.

print(sum(map(int, input().split())))
print('*' * 100)


# 1-6
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.

a, b = map(int, input().split())
print(a - b)
print('*' * 100)


# 1-7
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 AxB를 출력한다.

a, b = map(int, input().split())
print(a * b)
print('*' * 100)


# 1-8
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

a, b = map(int, input().split())
print(a / b)
print('*' * 100)


# 1-9
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b) # 몫
print(a % b) # 나머지
print('*' * 100)


# 1-10
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print(((a * b) % c))
print(((a % c) * (b % c)) % c)
print('*' * 100)


# 1-11
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

a = int(input())
b = input()
print(a * int(b[2]), a * int(b[1]), a * int(b[0]), a * int(b), sep='\n')
