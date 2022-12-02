N = int(input())  # 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
a = list(map(int, input().split()))  # 둘째 줄에는 정수가 공백으로 구분되어져있다.
v = int(input())  # 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
print(a.count(v))  # count()로 a list에 있는 v의 개수를 알려주기