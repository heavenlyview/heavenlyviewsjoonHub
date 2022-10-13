n = int(input())

fibo =[] #피보나치 수를 저장하는 리스트
fibo.append(0) #0과 1을 미리 저장
fibo.append(1)

for i in range(2, n+1): # 리스트에 피보나치 수를 계산하여 저장
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n]) # fibo 리스트의 마지막 인덱스 출력 -> n번째 피보나치 수가 출력됨
# print(fibo) #진짜 마지막에 있는지 확인해보기