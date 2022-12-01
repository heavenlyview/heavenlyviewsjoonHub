T = int(input()) # 테스트 케이스 T

for i in range(T):
  N = list(map(int, input().split()))

  N.pop(N.index(max(N))) # N에서 최고점만 빼내기
  N.pop(N.index(min(N))) # N에서 최저점만 빼내기

  if max(N) - min(N) >= 4:
# 위에서 최고점, 최저점 빼고난 후의 남은 정수들 중에서 최고점과 최저점 차이가 4점 이상이면
    print("KIN") # "KIN"을 출력해줘
  else:
    print(sum(N)) # 그게 아니라면 남은 정수들의 합을 출력해줘
