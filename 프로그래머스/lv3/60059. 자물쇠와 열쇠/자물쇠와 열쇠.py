# 자물쇠와 열쇠 # 90e도 회전 접근만 했으나 확장하는 것은 시도하지 못함 
# 자물쇠와 열쇠를 포개었을 때 자물쇠의 값이 1이면 즉, 모든 자물쇠의 값이 1이면 (2도 없으니까 열쇠랑 포개어지지도 않은 것)

# 2차원 리스트 90도 회전 
def rotate_matrix(a):
    n=len(a) #행 길이 계산
    m=len(a[0]) #열 길이 계산
    result=[[0]*n for _ in range(m)] # n ,m이 바뀌어있다고 생각할 수 있으나 회전된 행렬을 넣을 것이므로  
    for i in range (n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 전부 1인지 확인한다
# 자물쇠는 3배 확대할 거니까 

def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range (lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j]!=1:
                return False
    return True


def solution (key, lock):
    n = len(lock)
    m = len(key)
    new_lock= [[0] * n * 3 for _ in range (n*3)]
    for i in range (n):
        for j in range (n):
            new_lock[i+n][j+n]=lock[i][j]
    
    # 4번 열쇠를 회전해서 확인해야 한다 
    for rotate in range (4):
        key=rotate_matrix(key)
        for x in range (n * 2):
            for y in range (n * 2):
                # 자물쇠에 열쇠를 끼워넣기 
                for i in range (m):
                    for j in range (m):
                        new_lock[x+i][y+j]+=key[i][j] # 이 부분이 어려울 수 있는데 키를 움직이면서 움직일때 값이 변하는건 자물쇠이므로 
                                                        # x,y만큼 움직일때마다 자물쇠의 값이 바뀐다
                # x,y가 바뀔때가 열쇠를 움직일때마다 이므로 이 경우마다 열리는지 확인해야 한다 
                if check(new_lock)==True:
                    return True
                
                # 다음 움직여서 자물쇠의 값을 계산해야하므로 자물쇠의 값을 초기화 시켜야한다 
                for i in range (m):
                    for j in range (m):
                        new_lock[x+i][y+j]-=key[i][j] #
    
    return False # True값을 받지 못했다면 False 반환