def solution(name, yearning, photo):
    miss_point={}
    result = [0 for _ in range (len(photo))]
    for i in range (len(name)):
        miss_point[name[i]] = yearning[i]
    for i in range(len(photo)):
        for n in photo[i] :
            if n in miss_point:
                result[i] += miss_point[n]            
    
    return result