class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque 
        X, Y = len(image)-1, len(image[sr])-1                
        queue = deque()
        visited = set()
        queue.append((sr,sc))
                
        while queue:
            x, y = queue.popleft()
            visited.add((x,y))
            ogColor, image[x][y] = image[x][y], newColor
            
            if x < X:
                if image[x+1][y] == ogColor and (x+1, y) not in visited:
                    queue.append((x+1,y)) 
            if x > 0:
                if image[x-1][y] == ogColor and (x-1, y) not in visited:
                    queue.append((x-1,y))   
            if y < Y:
                if image[x][y+1] == ogColor and (x, y+1) not in visited:
                    queue.append((x,y+1))
            if y > 0:
                if image[x][y-1] == ogColor and (x, y-1) not in visited:
                    queue.append((x, y-1))
                
        return image