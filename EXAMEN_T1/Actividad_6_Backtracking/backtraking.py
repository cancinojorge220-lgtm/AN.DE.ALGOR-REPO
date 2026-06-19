from typing import List, Dict, Tuple, Any
class BusinessMaze:
    def __init__(self, grid: List[List[int]], max_budget: int):
        """
        :param grid: Matriz de costos (0 = Bloqueado, >=1 costo de paso).
        :param max_budget: Presupuesto máximo permitido de recursos/tiempo.
        """
        self.grid = grid
        self.max_budget = max_budget
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.directions = [
            (1, 0),  # Abajo
            (0, 1),  # Derecha
            (-1, 0),  # Arriba
            (0, -1)  # Izquierda
        ]

    def solve(self, start_row: int = 0, start_col: int = 0,
              end_row: int = None, end_col: int = None) -> List[Dict[str, Any]]:
        """
        Encuentra todas las soluciones viables que no superen el presupuesto.
        """
        if end_row is None:
            end_row = self.rows - 1
        if end_col is None:
            end_col = self.cols - 1

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        path = []
        solutions = []

        # Iniciamos la búsqueda recursiva
        self._backtrack(start_row, start_col, end_row, end_col, 0, visited, path, solutions)
        return solutions

    def _backtrack(self, r: int, c: int, end_r: int, end_c: int,
                   current_cost: int, visited: List[List[bool]],
                   path: List[Tuple[int, int]], solutions: List[Dict[str, Any]]) -> None:

        # 1. CASO BASE: Llegada al destino exitosa
        if r == end_r and c == end_c:
            final_cost = current_cost + self.grid[r][c]
            if final_cost <= self.max_budget:
                path.append((r, c))
                solutions.append({
                    "path": list(path),
                    "cost": final_cost
                })
                path.pop()  # Deshacer el último paso
            return

        # 2. CONTROLES DE FRONTERA Y VIABILIDAD
        # - Fuera de los límites de la grilla
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return

        # - Celda bloqueada (obstáculo/pared representada por 0)
        if self.grid[r][c] == 0:
            return

        # - Evitar ciclos (celda ya visitada en el camino actual)
        if visited[r][c]:
            return

        # 3. PODA POR RESTRICCIÓN (Pruning)
        # Si el costo de entrar a esta oficina supera el presupuesto disponible, abortamos la rama.
        step_cost = self.grid[r][c]
        if current_cost + step_cost > self.max_budget:
            return

        # 4. PASO DE EXPLORACIÓN (Marcar Estado)
        visited[r][c] = True
        path.append((r, c))

        # Explorar recursivamente las 4 direcciones
        for dr, dc in self.directions:
            self._backtrack(
                r + dr,
                c + dc,
                end_r,
                end_c,
                current_cost + step_cost,
                visited,
                path,
                solutions
            )

        # 5. RETROCESO (Backtrack - Desmarcar Estado)
        # Al regresar en la recursión, liberamos la celda para que otros caminos puedan usarla.
        path.pop()
        visited[r][c] = False


if __name__ == "__main__":
    # Grilla donde: 1 = Costo bajo, 5 = Trámite burocrático (Costo alto), 0 = Bloqueado
    grid = [
        [1, 1, 0, 1, 1],
        [0, 5, 1, 5, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 5, 1],
        [1, 1, 1, 1, 1]
    ]

    maze = BusinessMaze(grid, max_budget=20)
    solutions = maze.solve()

    print("--- SOLUCIONES ENCONTRADAS ---")
    for index, sol in enumerate(solutions):
        print(f"\nSolución {index + 1} (Costo Total: {sol['cost']}):")
        formatted_path = " -> ".join(f"({r},{c})" for r, c in sol["path"])
        print(formatted_path)
