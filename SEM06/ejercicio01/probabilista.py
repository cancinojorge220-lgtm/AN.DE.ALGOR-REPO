import random
import tkinter as tk
from tkinter import messagebox

class SimuladorSorteoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteo de Becas")
        self.root.geometry("520x420")

        self.estudiantes = []
        self.ganadores = []

        self.crear_interfaz()

    # Creación de la interfaz gráfica
    def crear_interfaz(self):
        frame_top = tk.Frame(self.root, padx=10, pady=10)
        frame_top.pack(fill="x")

        tk.Label(frame_top, text="Nombre Completo:", anchor="w").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_top, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5)

        btn_registrar = tk.Button(frame_top, text="Registrar", width=12, command=self.registrar_estudiante)
        btn_registrar.grid(row=0, column=2, padx=5)

        frame_lista = tk.Frame(self.root, padx=10, pady=5)
        frame_lista.pack(fill="both", expand=True)

        tk.Label(frame_lista, text="Participantes inscritos:", anchor="w").pack(anchor="w")
        self.lista_participantes = tk.Listbox(frame_lista, height=10, width=60)
        self.lista_participantes.pack(fill="both", expand=True)

        frame_info = tk.Frame(self.root, padx=10, pady=5)
        frame_info.pack(fill="x")

        self.lbl_total = tk.Label(frame_info, text="Total inscritos: 0")
        self.lbl_total.pack(side="left")

        self.lbl_probabilidad = tk.Label(frame_info, text="Probabilidad base: 0%")
        self.lbl_probabilidad.pack(side="right")

        frame_sorteo = tk.Frame(self.root, padx=10, pady=10)
        frame_sorteo.pack(fill="x")

        tk.Label(frame_sorteo, text="Cantidad de becas:").grid(row=0, column=0, sticky="w")
        self.entry_becas = tk.Entry(frame_sorteo, width=5)
        self.entry_becas.grid(row=0, column=1, padx=5)
        self.entry_becas.insert(0, "1")

        btn_sorteo = tk.Button(frame_sorteo, text="Realizar sorteo", width=14, command=self.realizar_sorteo)
        btn_sorteo.grid(row=0, column=2, padx=10)

        btn_reporte = tk.Button(frame_sorteo, text="Generar reporte", width=14, command=self.generar_reporte)
        btn_reporte.grid(row=0, column=3, padx=5)

        tk.Label(self.root, text="Ganadores:", anchor="w").pack(anchor="w", padx=10)
        self.txt_resultados = tk.Text(self.root, height=6, width=62)
        self.txt_resultados.pack(padx=10, pady=(0, 10))

    def registrar_estudiante(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning(
                "Nombre vacío", "Ingresa el nombre del estudiante."
            )
            return

        if nombre in self.estudiantes:
            messagebox.showwarning(
                "Estudiante repetido", "Ya registraste a este estudiante antes."
            )
            return

        self.estudiantes.append(nombre)
        self.lista_participantes.insert(tk.END, f"{len(self.estudiantes)}. {nombre}")

        self.entry_nombre.delete(0, tk.END)
        self.actualizar_estadisticas()

    def actualizar_estadisticas(self):
        total = len(self.estudiantes)
        self.lbl_total.config(text=f"Total Inscritos: {total}")

        if total > 0:
            prob = (1 / total) * 100
            self.lbl_probabilidad.config(text=f"Probabilidad base: {prob:.2f}%")
        else:
            self.lbl_probabilidad.config(text="Probabilidad base: 0%")

    def realizar_sorteo(self):
        if not self.estudiantes:
            messagebox.showerror(
                "Error", "Aún no hay estudiantes. Registra al menos uno antes de hacer el sorteo."
            )
            return

        try:
            cant_becas = int(self.entry_becas.get())
        except ValueError:
            messagebox.showerror(
                "Error", "La cantidad de becas tiene que ser un número entero."
            )
            return

        if cant_becas <= 0:
            messagebox.showerror(
                "Error", "Pon un número mayor que cero en la cantidad de becas, por favor."
            )
            return

        if cant_becas > len(self.estudiantes):
            messagebox.showerror(
                "Error",
                f"No hay suficientes estudiantes para sortear {cant_becas} becas."
            )
            return

        self.ganadores = random.sample(self.estudiantes, cant_becas)

        self.txt_resultados.delete("1.0", tk.END)
        self.txt_resultados.insert(tk.END, "¡Felicidades a los ganadores!\n")
        for i, ganador in enumerate(self.ganadores, 1):
            self.txt_resultados.insert(tk.END, f" Beca {i}: {ganador}\n")

    def generar_reporte(self):
        if not self.ganadores:
            messagebox.showwarning(
                "Sin resultados",
                "Todavía no hay ganadores. Primero haz el sorteo y luego generas el reporte.",
            )
            return

        nombre_archivo = "reporte_ganadores_becas.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write("REPORTE DE GANADORES DE BECAS\n")
                f.write("===========================\n")
                f.write(f"Total de alumnos que participaron: {len(self.estudiantes)}\n")
                f.write(f"Total de becas otorgadas: {len(self.ganadores)}\n\n")
                f.write("Lista de Ganadores:\n")
                for i, ganador in enumerate(self.ganadores, 1):
                    f.write(f"{i}. {ganador}\n")

            messagebox.showinfo(
                "Reporte listo",
                f"Ya está listo. Guardé el reporte como '{nombre_archivo}'."
            )
        except Exception as e:
            messagebox.showerror(
                "Error", "No pude guardar el reporte. Revisa si puedes escribir en esta carpeta."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorSorteoApp(root)
    root.mainloop()