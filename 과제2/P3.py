"""
**Instruction**
Please see instruction document.

"""

def P3(world: list):
    ##### Write your Code Here #####
    def bfs(world, i,j):
        def expand(queue, i,j):
            if i == M-1:
                if j == N-1:
                    queue.append((i-1,j))
                    queue.append((i,j-1))
                elif j == 0:
                    queue.append((i-1,j))
                    queue.append((i,j+1))
                else :
                    queue.append((i-1,j))
                    queue.append((i,j-1))
                    queue.append((i,j+1))
            elif i == 0:
                if j == N-1:
                    queue.append((i+1,j))
                    queue.append((i,j-1))
                elif j == 0:
                    queue.append((i+1,j))
                    queue.append((i,j+1))
                else :
                    queue.append((i+1,j))
                    queue.append((i,j-1))
                    queue.append((i,j+1))
            else :
                if j == 0:
                    queue.append((i-1,j))
                    queue.append((i+1,j))
                    queue.append((i,j+1))
                elif j == N-1:
                    queue.append((i-1,j))
                    queue.append((i+1,j))
                    queue.append((i,j-1))
                else :
                    queue.append((i-1,j))
                    queue.append((i+1,j))
                    queue.append((i,j-1))
                    queue.append((i,j+1))
                
                
        def visit(i,j):
            if world[i][j] == 0:
                return False
            else:
                world[i][j] = 0 # visit mark
                return True
                
                
        queue = []
        visit(i,j)
        expand(queue,i,j)
        while queue:
            idx = queue.pop(0)
            if visit(idx[0], idx[1]):
                expand(queue, idx[0], idx[1])
            
        
        
    M, N = len(world), len(world[0])
    
    island = 0
    for i in range(M):
        for j in range(N):
            if world[i][j] == 1:
                bfs(world, i,j)
                island += 1
                
            else:
                pass
    return island
            
        

    ##### End of your code ##### 
    
if __name__ == '__main__':
    ex1 = [[1,1,1,1,0], 
           [1,0,0,1,0],
           [1,1,0,1,0],
           [1,1,0,0,0]]
    
    ex2 = [[1,1,0,0,0],
           [1,1,0,0,0],
           [0,0,1,1,0],
           [0,0,0,0,1]]
    
    ex3 = [[0,1,0,1,0,1]]
    
    ex4 = [[1],
           [0],
           [1]]
    print(P3(ex1))
    print(P3(ex2))
    print(P3(ex3))
    print(P3(ex4))