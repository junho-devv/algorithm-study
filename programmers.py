def solution(n):

    answer = 0
    
    for x in range(2, n+1):
        cnt = 0

        for y in range(1, x+1):
            if x % y == 0:
                cnt += 1

        if cnt == 2:
            answer += 1    

    return answer
def solution002():
    val = input()
    row = int(val[1])
    col = int(ord(val[0])) - int(ord('a')) + 1
    
    count = 0

    print(row, col)
    
    moves = [ (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1) ]
    
    for move in moves:
        nRow = row + move[1]
        nCol = col + move[0]
        
        if nCol > 0 and nRow > 0 and nCol < 9 and nRow < 9:
            count += 1
    
    print(count)

#n = int(input())
#print(solution(n))

solution002()