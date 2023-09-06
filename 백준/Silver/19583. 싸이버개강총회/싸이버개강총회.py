# 사이버개강총회
# 누가 개강총회 왔는지 알 수 없다, 누가 끝까지 남았는지 알 수 없다, 단순히 스트리밍 틀어놓는지를 알 수 없다
# 개강총회 시작 전, 학회원 입장 여부 확인 , 개강총회 시작 시간 전 대화여부로 체크, 개강총회 시작하자마자 채팅도 입장 확인
# 개강총회를 끝내고 나서, 스트리밍이 끝날때 까지  
# 즉 개강총회 끝~ 스트리밍끝날때까지 대화 했거나, 개강총회 끝나자마자 채팅, 개강총회 스트리밍이 끝나자마자 채팅도 제시간에 퇴장
# 즉 입장여부는 개강총회시간보다 작을때 입장했어야하고
# 개강총회 끝시간~ 개강총회 스트리밍 끝시간 까지 채팅 남기면 된다
import sys
s, e, q= input().split()
s = int(s.replace(":", ""))
e = int(e.replace(":", ""))
q = int(q.replace(":", ""))
chats=[]
check={}
for line in sys.stdin:
    time, name = line.split()
    time = int(time.replace(":", ""))
    chats.append((time, name))
for i in chats: # 출석여부 확인
    if i[1] in check:
        continue
    if i[0] <= s:
        check[i[1]] = 1

for i in chats: # 퇴장여부 확인 (출석된 애들중에서만 확인하면 된다)
    if e <= i[0] <= q :
        if i[1] in check:
            check[i[1]] += 1
cnt = 0
for i in (check.values()):
    if i >=2:
        cnt += 1
print(cnt)
