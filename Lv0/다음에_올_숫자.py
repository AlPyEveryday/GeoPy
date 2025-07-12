def solution(common):
    if common[1]-common[0] == common[2]-common[1]:
        return common[0]+len(common)*(common[1]-common[0])
    else:
        return common[0]*(common[1]/common[0])**len(common)
    
#신기한 풀이
def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1] : #등차수열
        return common.pop()+common[1]-common[0]
    else : #등비수열
        return common.pop()*common[1]//common[0]
    return answer