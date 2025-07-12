def solution(lines):
    visit = {i: 0 for i in range(-100, 101)}
    cnt = 0
    
    for line in lines:
        for i in range(line[0], line[1]): 
            visit[i] += 1

    for i in range(-100, 101):
        if visit[i] >= 2: 
            cnt += 1

    return cnt
