class Solution:
    ROTTEN = 2
    FRESH = 1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        visited = set()
        
        for x,y in self.getOs(grid, Solution.ROTTEN):
            queue.append((x,y))
            visited.add((x,y))
        
		#Check if the grid is valid if no rotten oranges
        freshCount = 0
        for _ in self.getOs(grid, Solution.FRESH):
            freshCount += 1
        if not queue:
            return 0 if freshCount == 0 else -1
            
        m, n =len(grid), len(grid[0])
        minutes = -1
        while queue:
            minutes += 1
            num_r = len(queue)
            for _ in range(num_r):
                ro = queue.popleft()
                for afo in self.getAdjOs(ro[0], ro[1], m - 1, n - 1):
                    if grid[afo[0]][afo[1]] == Solution.FRESH and (afo[0], afo[1]) not in visited:
                        queue.append((afo[0], afo[1]))
                        visited.add((afo[0], afo[1]))
                        
        return minutes if self.checkGrid(grid, visited) else -1

    def checkGrid(self, grid, visited):
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and (x,y) not in visited:
                    return False
        return True
                    
    def getAdjOs(self, x, y, maxX, maxY):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for dire in directions:
            newX, newY = x + dire[0], y + dire[1]
            if 0 <= newX <= maxX and 0<= newY <= maxY:
                yield (newX, newY)
                
    def getOs(self, grid, orangeType):
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == orangeType:
                    yield (x,y)