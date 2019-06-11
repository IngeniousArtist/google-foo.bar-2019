chess = [
	[ 0, 1, 2, 3, 4, 5, 6, 7],
	[ 8, 9,10,11,12,13,14,15],
	[16,17,18,19,20,21,22,23],
	[24,25,26,27,28,29,30,31],
	[32,33,34,35,36,37,38,39],
	[40,41,42,43,44,45,46,47],
	[48,49,50,51,52,53,54,55],
	[56,57,58,59,60,61,62,63]
	] 

def findindex(val):
	for i in range(0,8):
		for j in range(0,8):
			if chess[i][j] == val:
				k = [i,j]
				return k

class cell: 
      
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
def isInChess(x, y): 
    if (x >= 0 and x < 8 and y >= 0 and y < 8):  
        return True
    return False
      
def steps(kp,tp): 

    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    queue = [] 
    queue.append(cell(kp[0], kp[1], 0)) 

    visited = [[False for i in range(0,8)] for j in range(0,8)] 

    visited[kp[0]][kp[1]] = True 
    while(len(queue) > 0): 
          
        t = queue[0] 
        queue.pop(0) 
           
        if(t.x == tp[0] and 
           t.y == tp[1]): 
            return t.dist 
              
        for i in range(0,8): 
              
            x = t.x + dx[i] 
            y = t.y + dy[i] 
              
            if(isInChess(x, y) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1)) 

def solution(src, dest):
	s = findindex(src)
	d = findindex(dest)
	kp = s 
	tp = d 
	return steps(kp,tp) 

"""
TESTING
==================
a = solution(0,1)
print(a)
b = solution(19,36)
print(b)
"""
