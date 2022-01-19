class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_length=0
        r=len(grid)
        c=len(grid[0])
        visited=[ [0] * c for i1 in range(r) ]
        for i in range(r):
            for j in range(c):
                if(visited[i][j]==0 and grid[i][j]==1):
                    l=0
                    q=[(i,j)]
                    while(len(q)!=0):
                        x=q.pop(0)
                        a=x[0]
                        b=x[1]
                        check=[(a-1,b),(a,b-1),(a,b+1),(a+1,b)]
                        for y in check:
                            if((y[0]>=0) and (y[0]<=r-1) and (y[1]>=0) and (y[1]<=c-1) and (grid[y[0]][y[1]]==1) and (visited[y[0]][y[1]]==0) and (y[0],y[1]) not in q):
                                q.append(y)
                        visited[a][b]=1
                        l+=1
                        #print(q)
                    print(l,i,j)
                    if(l>max_length):
                        max_length=l
        return(max_length)