N = int(input())          # 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
a = list(map(int, input().split())) # 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
print(min(a), max(a))