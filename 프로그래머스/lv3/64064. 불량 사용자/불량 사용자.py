from itertools import permutations
# 순열을 이용하는데 #가능한 경우만큼 유저를 뽑고 비교한다
def check(users, banned_id):
    # user ban 아이디의 길이가 같지 않으면 아예 불가능
    # 순열이니까 이렇게 비교가능 a,b / b,a랑도 어차피 모두 비교가 가능하므로 
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        # 길이가 같다면 별을 제외하고 모두 같아야하므로 별인경우는 무시하고 같은지 확인한다 
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)