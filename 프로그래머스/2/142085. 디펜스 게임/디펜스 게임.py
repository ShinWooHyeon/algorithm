'''
병사 n명 매라운드마다 enemy[i] 등장
남은 병사 중 enemy[i]명 만큼 소모해야 막을 수 있다
남은 병사수보다 현재 라운드 적의 수가 더 많으면 게임 종료
무적권 최대 k번 사용 가능 => 무적권 사용하는 위치를 알아야한다
크기 큰 순서로 3번 

'''
import heapq
def solution(n, k, enemy):
    save_q=[]
    if k >= len(enemy):
        return len(enemy)
    else:
        r = 0
        use = 0
        while use <= k and r <= (len(enemy) -1):
            heapq.heappush(save_q, (-enemy[r], r))
            if n >= enemy[r]:
                n-= enemy[r]
                r += 1
            else:
                if use == k:
                    return r 
                else:
                    use += 1
                    cand = heapq.heappop(save_q)
                    n = n - cand[0] - enemy[r]
                    r+= 1
        # while문이 성공적으로 다 돌았으면 
        return len(enemy)