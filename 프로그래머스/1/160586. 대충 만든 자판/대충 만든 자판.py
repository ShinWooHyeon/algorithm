# 키를 최소 몇번 눌러야 target이 될 수 있ㄴㄴ가?
from string import ascii_uppercase
def solution(keymap, targets):
    # target 값을 split 해서 돌리는데 없으면 -1 하고 return한다
    # keymap에서 알파벳별 dictionary 값을 갱신해야 하네 
    key_dic = {}
    upper_case = list(ascii_uppercase)
    for alpha in upper_case:
        key_dic[alpha] = 1e9
    for keystr in keymap:
        for i in range (len(keystr)):
            # 현재 keystr의 문자열을 누르기 위한 횟수가 dic에 기록된 횟수보다 적다면 갱신
            if i + 1  < key_dic[keystr[i]]:
                key_dic[keystr[i]] = i + 1
    answer = []
    for target in targets:
        cnt = 0
        possible = True
        for i in range(len(target)):
            if key_dic[target[i]] != 1e9:
                cnt += key_dic[target[i]]
            else:
                possible = False
                break
        if not possible:
            answer.append(-1)
        else:
            answer.append(cnt)

    return answer