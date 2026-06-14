import tkinter as tk
from tkinter import ttk, messagebox


class HanoiFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.n_var = tk.IntVar(value=4)
        self.speed_var = tk.IntVar(value=400)

        self.rods = []
        self.moves = []
        self.current_move = 0
        self.running = False

        controls = ttk.Frame(self)
        controls.pack(pady=10)

        ttk.Label(controls, text="Discos:").grid(row=0, column=0, padx=5)
        ttk.Spinbox(
            controls,
            from_=1,
            to=8,
            textvariable=self.n_var,
            width=5
        ).grid(row=0, column=1, padx=5)

        ttk.Label(controls, text="Velocidad ms:").grid(row=0, column=2, padx=5)
        ttk.Spinbox(
            controls,
            from_=50,
            to=1500,
            increment=50,
            textvariable=self.speed_var,
            width=7
        ).grid(row=0, column=3, padx=5)

        ttk.Button(controls, text="Reiniciar", command=self.reset).grid(row=0, column=4, padx=5)
        ttk.Button(controls, text="Resolver", command=self.start_solution).grid(row=0, column=5, padx=5)

        self.info_label = ttk.Label(self, text="")
        self.info_label.pack()

        self.canvas = tk.Canvas(self, width=750, height=380, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.reset()

    def reset(self):
        self.running = False
        n = self.n_var.get()

        # Cada torre guarda discos. El número más grande representa un disco más grande.
        self.rods = [
            list(range(n, 0, -1)),
            [],
            []
        ]

        self.moves = []
        self.current_move = 0
        self.draw()

    def generate_hanoi_moves(self, n, origin, auxiliary, destination):
        if n == 1:
            self.moves.append((origin, destination))
        else:
            self.generate_hanoi_moves(n - 1, origin, destination, auxiliary)
            self.moves.append((origin, destination))
            self.generate_hanoi_moves(n - 1, auxiliary, origin, destination)

    def start_solution(self):
        if self.running:
            return

        self.reset()
        n = self.n_var.get()

        self.generate_hanoi_moves(n, 0, 1, 2)
        self.running = True
        self.animate_solution()

    def animate_solution(self):
        if not self.running:
            return

        if self.current_move >= len(self.moves):
            self.running = False
            messagebox.showinfo("Torres de Hanoi", "Solución completada.")
            return

        origin, destination = self.moves[self.current_move]

        disk = self.rods[origin].pop()
        self.rods[destination].append(disk)

        self.current_move += 1
        self.draw()

        self.after(self.speed_var.get(), self.animate_solution)

    def draw(self):
        self.canvas.delete("all")

        n = self.n_var.get()
        width = 750
        height = 380

        base_y = 320
        peg_height = 220
        peg_width = 10

        peg_x = [180, 375, 570]

        self.canvas.create_rectangle(80, base_y, 670, base_y + 12, fill="black")

        for i, x in enumerate(peg_x):
            self.canvas.create_rectangle(
                x - peg_width // 2,
                base_y - peg_height,
                x + peg_width // 2,
                base_y,
                fill="gray"
            )
            self.canvas.create_text(x, base_y + 35, text=f"Torre {i + 1}", font=("Arial", 11))

        max_disk_width = 150
        min_disk_width = 40
        disk_height = 22

        colors = [
            "#e74c3c", "#3498db", "#2ecc71", "#f1c40f",
            "#9b59b6", "#e67e22", "#1abc9c", "#34495e"
        ]

        for rod_index, rod in enumerate(self.rods):
            x = peg_x[rod_index]

            for level, disk_size in enumerate(rod):
                disk_width = min_disk_width + (disk_size - 1) * (
                        (max_disk_width - min_disk_width) / max(1, n - 1)
                )

                y = base_y - disk_height * (level + 1)

                self.canvas.create_rectangle(
                    x - disk_width / 2,
                    y,
                    x + disk_width / 2,
                    y + disk_height,
                    fill=colors[(disk_size - 1) % len(colors)],
                    outline="black"
                )

                self.canvas.create_text(
                    x,
                    y + disk_height / 2,
                    text=str(disk_size),
                    fill="white",
                    font=("Arial", 10, "bold")
                )

        total_moves = 2 ** n - 1
        self.info_label.config(
            text=f"Movimientos: {self.current_move} / {total_moves}"
        )

class KnightTourFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.size_var = tk.IntVar(value=5)
        self.start_row_var = tk.IntVar(value=0)
        self.start_col_var = tk.IntVar(value=0)
        self.speed_var = tk.IntVar(value=150)

        self.board = []
        self.path = []
        self.current_step = 0
        self.running = False

        controls = ttk.Frame(self)
        controls.pack(pady=10)

        ttk.Label(controls, text="Tamaño tablero:").grid(row=0, column=0, padx=5)
        ttk.Spinbox(
            controls,
            from_=5,
            to=8,
            textvariable=self.size_var,
            width=5
        ).grid(row=0, column=1, padx=5)

        ttk.Label(controls, text="Fila inicial:").grid(row=0, column=2, padx=5)
        ttk.Spinbox(
            controls,
            from_=0,
            to=7,
            textvariable=self.start_row_var,
            width=5
        ).grid(row=0, column=3, padx=5)

        ttk.Label(controls, text="Columna inicial:").grid(row=0, column=4, padx=5)
        ttk.Spinbox(
            controls,
            from_=0,
            to=7,
            textvariable=self.start_col_var,
            width=5
        ).grid(row=0, column=5, padx=5)

        ttk.Label(controls, text="Velocidad ms:").grid(row=0, column=6, padx=5)
        ttk.Spinbox(
            controls,
            from_=20,
            to=1000,
            increment=20,
            textvariable=self.speed_var,
            width=7
        ).grid(row=0, column=7, padx=5)

        ttk.Button(controls, text="Resolver", command=self.solve).grid(row=0, column=8, padx=5)
        ttk.Button(controls, text="Limpiar", command=self.clear_board).grid(row=0, column=9, padx=5)

        self.info_label = ttk.Label(self, text="")
        self.info_label.pack()

        self.canvas = tk.Canvas(self, width=560, height=560, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.clear_board()

    def clear_board(self):
        self.running = False
        n = self.size_var.get()

        self.board = [[-1 for _ in range(n)] for _ in range(n)]
        self.path = []
        self.current_step = 0
        self.draw_board()

    def is_valid(self, row, col):
        n = self.size_var.get()

        return (
                0 <= row < n and
                0 <= col < n and
                self.board[row][col] == -1
        )

    def possible_moves(self, row, col):
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        valid_moves = []

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if self.is_valid(new_row, new_col):
                valid_moves.append((new_row, new_col))

        # Heurística de Warnsdorff:
        # Se prueban primero las casillas que tienen menos movimientos posibles.
        valid_moves.sort(key=lambda move: self.count_future_moves(move[0], move[1]))

        return valid_moves

    def count_future_moves(self, row, col):
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        count = 0

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if self.is_valid(new_row, new_col):
                count += 1

        return count

    def knight_tour_backtracking(self, row, col, step):
        n = self.size_var.get()

        self.board[row][col] = step
        self.path.append((row, col))

        if step == n * n - 1:
            return True

        for new_row, new_col in self.possible_moves(row, col):
            if self.knight_tour_backtracking(new_row, new_col, step + 1):
                return True

        # Backtracking: si no sirve esta ruta, se deshace el movimiento.
        self.board[row][col] = -1
        self.path.pop()

        return False

    def solve(self):
        if self.running:
            return

        n = self.size_var.get()
        start_row = self.start_row_var.get()
        start_col = self.start_col_var.get()

        if start_row >= n or start_col >= n:
            messagebox.showerror(
                "Error",
                "La fila y columna inicial deben estar dentro del tablero."
            )
            return

        self.clear_board()

        found = self.knight_tour_backtracking(start_row, start_col, 0)

        if not found:
            messagebox.showwarning(
                "Salto del caballo",
                "No se encontró solución desde esa posición."
            )
            return

        self.current_step = 0
        self.running = True
        self.animate_path()

    def animate_path(self):
        if not self.running:
            return

        if self.current_step >= len(self.path):
            self.running = False
            messagebox.showinfo("Salto del caballo", "Recorrido completado.")
            return

        self.draw_board(animated_until=self.current_step)
        self.current_step += 1

        self.after(self.speed_var.get(), self.animate_path)

    def draw_board(self, animated_until=None):
        self.canvas.delete("all")

        n = self.size_var.get()
        canvas_size = 560
        cell_size = canvas_size / n

        if animated_until is None:
            animated_until = -1

        # Dibuja tablero
        for row in range(n):
            for col in range(n):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="black"
                )

        # Dibuja recorrido hasta el paso animado
        for step in range(animated_until + 1):
            row, col = self.path[step]

            x = col * cell_size + cell_size / 2
            y = row * cell_size + cell_size / 2

            self.canvas.create_oval(
                x - cell_size * 0.28,
                y - cell_size * 0.28,
                x + cell_size * 0.28,
                y + cell_size * 0.28,
                fill="#2c3e50",
                outline="white",
                width=2
            )

            self.canvas.create_text(
                x,
                y,
                text=str(step + 1),
                fill="white",
                font=("Arial", int(cell_size / 4), "bold")
            )

        # Dibuja líneas del recorrido
        for step in range(animated_until):
            row1, col1 = self.path[step]
            row2, col2 = self.path[step + 1]

            x1 = col1 * cell_size + cell_size / 2
            y1 = row1 * cell_size + cell_size / 2
            x2 = col2 * cell_size + cell_size / 2
            y2 = row2 * cell_size + cell_size / 2

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="red",
                width=2
            )

        total = n * n
        current = max(0, animated_until + 1)

        self.info_label.config(
            text=f"Casillas visitadas: {current} / {total}"
        )


class BacktrackingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Algoritmos de Backtracking")
        self.geometry("820x720")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        hanoi_tab = HanoiFrame(notebook)
        knight_tab = KnightTourFrame(notebook)

        notebook.add(hanoi_tab, text="Torres de Hanoi")
        notebook.add(knight_tab, text="Salto del caballo")


if __name__ == "__main__":
    app = BacktrackingApp()
    app.mainloop()
