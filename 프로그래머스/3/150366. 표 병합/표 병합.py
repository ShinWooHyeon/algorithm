'''
UPDATE r c value  => r,c 셀 값value로 바꾼다
UPDATE value1 value2 => value1 값 전부 value 2로 바꾼다
MERGE r1 c1 r2 c2 
=> 같은 셀일경우 무시, 인접하지 않으면 사이 셀 고려 안하고 두 셀만 병합, 한 셀만 값 가지고 있으면 병합된
셀은 그 값을 가진다. 모두 값을 가지면 r1, c1의 값을 가진다.
이후 r1,c1과 r2,c2 어느 위치를 선택해도 병합된 셀로 접근

UNMERGE r c => 해당 셀이 포함된 모든 셀은 프로그램 실행 초기 상태로 돌아간다 , 병합 해제전 셀의 값을 r,c가 갖게 된다

PRINT RC => r,c의 셀을 선택하여 셀의 값을 출력한다, 선택한 셀이 비어있을 경우 EMPTY 출력한다 

'''
# category
def solution(commands):
    # 50 * 50 셀 초기 상태 (전부 값 X) , 편의 위해 51로
    # 병합된 셀을 리스트로 다뤄야 한다 
    answer = []
    board = [[None for _ in range (51)] for _ in range(51)]
    merge_board=[[False for _ in range(51)] for _ in range (51)]
    for order in commands:
        ol = order.split()
        if ol[0] == 'UPDATE' :
            # r, c, 값 갱신이면 셀이면 해당되는 셀 전체 변경, 아니면 r,c만 변경인데 
            if len(ol) == 4:
                r, c, value = int(ol[1]), int(ol[2]), ol[3]
                # 병합되지 않았다면
                if merge_board[r][c] == False:
                    board[r][c] = value
                # 병합된 경우 해당 병합된 셀 전체를 r,c로 바꿔줘야한다 
                # 병합된 셀의 포함하고 있는 셀의 인덱스를 전부 저장해야 한다
                else:
                    cell_list = merge_board[r][c]
                    for cell in cell_list:
                        x, y = cell
                        board[x][y] = value
            elif len(ol) == 3:
                value1, value2 = ol[1], ol[2]
                for i in range (1, 51):
                    for j in range (1, 51):
                        if board[i][j] == value1:
                            board[i][j] = value2
        # 병합일경우
        elif ol[0] == 'MERGE' :
            r1, c1, r2, c2 = int(ol[1]), int(ol[2]), int(ol[3]), int(ol[4])
            # 두 셀이 이미 같은 셀로 병합되어 있을 경우 무시한다
            if merge_board[r1][c1] == merge_board[r2][c2] and merge_board[r1][c1] != False:
                continue
            # 일단 r1, c1 / r2, c2 중 병합된 셀이 있으면 전부 병합 후보에 넣어줘야 한다 
            else:
                merge_cand = []
                if merge_board[r1][c1] != False:
                    merge_cand += merge_board[r1][c1]
                else:
                    merge_cand.append((r1, c1))
                if merge_board[r2][c2] != False:
                    merge_cand += merge_board[r2][c2]
                else:
                    merge_cand.append((r2, c2))
                # merge_board와 board를 전부 갱신해준다
                merge_value = None
                if board[r1][c1] != None:
                    merge_value = board[r1][c1]
                else:
                    if board[r2][c2] != None:
                        merge_value = board[r2][c2]
                for x, y in merge_cand:
                    board[x][y] = merge_value
                    merge_board[x][y] = merge_cand
                # 이 과정 지나면 merge_board의 병합된 셀들을 전부 같은 인덱스 리스트들을 값으로 갖는다
        elif ol[0] == 'UNMERGE':
            r, c = int(ol[1]), int(ol[2])
            if merge_board[r][c] != False:
                if board[r][c] != None:
                    c_value = board[r][c]
                else:
                    c_value= None
                unmerge_list = merge_board[r][c]
                for x , y in unmerge_list:
                    board[x][y] = None
                    merge_board[x][y] = False
                board[r][c] = c_value
        elif ol[0] == 'PRINT':
            r, c = int(ol[1]), int(ol[2])
            if board[r][c] != None:
                answer.append(board[r][c])
            else:
                answer.append('EMPTY')

    return answer