import heapq    

class MazeSolver:
    def __init__(self, maze):
        """
        0 = Empty space
        1 = Wall
        'S' = Start
        'G' = Goal
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self._find_position('S')
        self.goal = self._find_position('G')
        
    def _find_position(self, target):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == target:
                    return (r, c)
        raise ValueError(self.maze, f"Target '{target}' not found in the maze.")

    def _heuristic(self, node):
        # Manhattan Distance Heuristic
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def _get_neighbors(self, node):
        r, c = node
        neighbors = []
        # Up, Down, Left, Right movements
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.maze[nr][nc] != 1: # Not a wall
                    neighbors.append((nr, nc))
        return neighbors

    def a_star_search(self):
        if not self.start or not self.goal:
            return None

        # Priority Queue elements: (f_score, current_node)
        open_set = []
        heapq.heappush(open_set, (0 + self._heuristic(self.start), self.start))
        
        # Tracking maps
        came_from = {}
        g_score = {self.start: 0}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            # Goal reached -> reconstruct path
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1] # Return reversed path
                
            for neighbor in self._get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self._heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, neighbor))
                    
        return None # Path unreachable

    def visualize_path(self, path):
        if not path:
            print("\n❌ No path found to the destination (Goal is unreachable).")
            return
            
        # Create a deep copy of the layout to draw the path line
        display_maze = [list(row) for row in self.maze]
        
        # Mark path nodes with '*' except start and goal
        for r, c in path:
            if display_maze[r][c] not in ('S', 'G'):
                display_maze[r][c] = '*'
                
        print(f"\n✅ Shortest Path Found! (Length: {len(path)} steps)")
        print("Legend: [S]: Start  |  [G]: Goal  |  [*]: Path  |  [█]: Wall\n")
        
        for row in display_maze:
            line = ""
            for item in row:
                if item == 1:
                    line += "█ "
                elif item == 0:
                    line += ". "
                else:
                    line += f"{item} "
            print(line)

# ==========================================
# TEST RUN VALIDATION
# ==========================================
if __name__ == "__main__":
    # 0 = Path, 1 = Wall, 'S' = Start, 'G' = Goal
    sample_maze = [
        ['S', 0, 1, 0, 0],
        [ 0 , 1, 0, 0, 1],
        [ 0 , 0, 0, 1, 'G'],
        [ 1 , 1, 0, 0, 0],
        [ 0 , 0, 0, 1, 0]
    ]
    
    # Instance initialization 
    solver = MazeSolver(sample_maze)
    shortest_path = solver.a_star_search()
    solver.visualize_path(shortest_path)
