from copy import deepcopy
def solution(players, callings):
    # players와 player dic을 잘 활용해야 한다 
    player_dic = {}
    for i in range (len(players)) :
        player_dic[players[i]] = i
    # player dic은 현재 순위
    for call in callings:
        rank = player_dic[call]
        # player리스트는 순위에 이름이 맵핑되있다
        # player_rank -1 한 이름이 call한 애와 바뀔 이름
        player_dic[call], player_dic[players[rank-1]] = player_dic[players[rank-1]],player_dic[call]
        players[rank -1], players[rank] = players[rank] , players[rank -1]
    return players