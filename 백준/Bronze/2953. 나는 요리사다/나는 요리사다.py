score = []

for i in range(5):   # for문을 5번 돌아서 참가자들 꺼 다 더해준다.
  score.append(sum(map(int, input().split())))  # score에 sum메서드해준걸 추가해준다.
print(score.index(max(score))+1, max(score)) # 우승자 번호, 우승자 점수 출력