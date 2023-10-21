'''
처음 나온거면 -1 
'''
def solution(s):
    alpha_idx = {}
    answer =[]
    for i in range(len(s)):
        if s[i] not in alpha_idx:
            alpha_idx[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - alpha_idx[s[i]])
            alpha_idx[s[i]] = i
    return answer