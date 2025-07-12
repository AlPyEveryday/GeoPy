def solution(num, total):
    arr=[]
    if num % 2 == 1:
        for i in range (num):
            arr.append(total/num-(num//2)+i) ## 3 - 2  + i
    else:
        for i in range (num):
            arr. append(total//num-(num//2)+1+i)    ## 3 - 2 + 1
    return arr            

#다른 풀이
def solution(num, total):
    if num % 2 == 1:
        return list(range(total//num-num//2, total//num+num//2+1))
    else:
        return list(range(total//num-num//2+1, total//num+num//2+1))