A = []
people_result = 0   # 초기화 먼저 해주고 시작
for i in range(4) : 
    Out_people, In_people = map(int, input().split()) # 내린 사람, 탄 사람 순서 대로 입력
    people_result += In_people   # 탄 사람이 입력되면 people_result 변수값 추가
    people_result -= Out_people  # 반대로 내린 사람이 입력되면 people_result 변수값 차감
    
    A.append(people_result)

print(max(A))  # 최댓값 구할거니까 max함수 이용해서 이 중에 최댓값 구해줘