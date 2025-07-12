def solution(board):
    ans=0
    n = len(board)
    arr = [[0] * n for _ in range(n)]

    for i in range(n):           
        for j in range(n):    
            if board[i][j] == 1:
                color(arr,i,j)
    
    for i in range(n):
        for j in range(n):            
            if arr[i][j] == 0:
                ans += 1
                
    return ans
            
def color(arr, i, j):
    n = len(arr)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1,  0,  1, -1, 1, -1, 0, 1]

    arr[i][j] = 1

    for d in range(8):
        ni = i + dx[d]
        nj = j + dy[d]

        if 0 <= ni < n and 0 <= nj < n:
            arr[ni][nj] = 1

    