import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FraudDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Detector Probabilista de Fraudes Bancarios")
        self.root.geometry("850x600")
        
        self.history = []
        self.risk_counts = {"Bajo": 0, "Medio": 0, "Alto": 0}
        
        # UI Elements
        self.setup_ui()
        
    def setup_ui(self):
        # Formulario
        form_frame = ttk.LabelFrame(self.root, text="Ingreso de Transacción")
        form_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(form_frame, text="Monto ($):").grid(row=0, column=0, padx=5, pady=5)
        self.monto_var = tk.DoubleVar()
        ttk.Entry(form_frame, textvariable=self.monto_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Hora (0-23):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_var = tk.IntVar()
        ttk.Entry(form_frame, textvariable=self.hora_var).grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Frecuencia (últimas 24h):").grid(row=1, column=0, padx=5, pady=5)
        self.frecuencia_var = tk.IntVar()
        ttk.Entry(form_frame, textvariable=self.frecuencia_var).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Ubicación:").grid(row=1, column=2, padx=5, pady=5)
        self.ubicacion_var = tk.StringVar(value="Local")
        ubicacion_combo = ttk.Combobox(form_frame, textvariable=self.ubicacion_var, values=["Local", "Nacional Inusual", "Internacional"])
        ubicacion_combo.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Button(form_frame, text="Analizar Riesgo", command=self.analizar).grid(row=2, column=0, columnspan=4, pady=10)
        
        # Resultados
        res_frame = ttk.Frame(self.root)
        res_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(res_frame, text="Nivel de Riesgo:", font=("Arial", 12, "bold")).pack(side="left")
        self.risk_label = tk.Label(res_frame, text="N/A", font=("Arial", 12, "bold"), width=15)
        self.risk_label.pack(side="left", padx=10)
        
        self.prob_label = ttk.Label(res_frame, text="Probabilidad: 0%", font=("Arial", 12))
        self.prob_label.pack(side="left", padx=10)
        
        # Historial y Gráfico
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview (Historial)
        tree_frame = ttk.Frame(bottom_frame)
        tree_frame.pack(side="left", fill="both", expand=True)
        
        ttk.Label(tree_frame, text="Historial de Operaciones").pack()
        columns = ("Monto", "Hora", "Frec", "Ubicación", "Riesgo")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)
        self.tree.pack(fill="both", expand=True)
        
        # Matplotlib Figure (Estadísticas)
        self.graph_frame = ttk.Frame(bottom_frame)
        self.graph_frame.pack(side="left", fill="both", expand=True, padx=10)
        
        self.fig, self.ax = plt.subplots(figsize=(3, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Reporte de transacciones sospechosas
        report_frame = ttk.Frame(bottom_frame)
        report_frame.pack(side="right", fill="both", expand=True)
        ttk.Label(report_frame, text="Reporte de Transacciones Sospechosas").pack()
        self.reporte_text = tk.Text(report_frame, height=10, width=35)
        self.reporte_text.pack(fill="both", expand=True)
        
        self.update_graph()

    def analizar(self):
        monto = self.monto_var.get()
        hora = self.hora_var.get()
        frecuencia = self.frecuencia_var.get()
        ubicacion = self.ubicacion_var.get()
            
        # Modelo Probabilista (Naive Bayes simplificado)
        # Probabilidad a priori de fraude: 1%
        prob_fraude = 0.01
        
        # Factor Monto: Transacciones grandes son más riesgosas
        if monto > 10000:
            prob_fraude *= 10
        elif monto > 3000:
            prob_fraude *= 3
            
        # Factor Hora: Transacciones de madrugada tienen más peso
        if 0 <= hora <= 5:
            prob_fraude *= 5 
            
        # Factor Frecuencia: Alta cantidad de operaciones en corto tiempo
        if frecuencia > 10:
            prob_fraude *= 8
        elif frecuencia > 5:
            prob_fraude *= 3
            
        # Factor Ubicación: Conexiones o ubicaciones inusuales
        if ubicacion == "Internacional":
            prob_fraude *= 6
        elif ubicacion == "Nacional Inusual":
            prob_fraude *= 2
            
        # Limitar probabilidad al 99.9%
        prob_fraude = min(0.999, prob_fraude)
        
        # Clasificar Riesgo
        if prob_fraude < 0.10:
            riesgo = "Bajo"
            color = "lightgreen"
        elif prob_fraude < 0.50:
            riesgo = "Medio"
            color = "gold"
        else:
            riesgo = "Alto"
            color = "tomato"
            
        # Actualizar Interfaz con Resultados
        self.risk_label.config(text=riesgo, bg=color)
        self.prob_label.config(text=f"Probabilidad: {prob_fraude*100:.1f}%")
        
        # Agregar al historial
        self.history.append((monto, hora, frecuencia, ubicacion, riesgo))
        self.tree.insert("", "end", values=(f"${monto:.2f}", f"{hora}:00", frecuencia, ubicacion, riesgo))
        
        # Actualizar estadisticas y grafico
        self.risk_counts[riesgo] += 1
        self.update_graph()
        
        # Alerta de reporte de transacción sospechosa
        if riesgo == "Alto":
            self.reporte_text.insert(tk.END, f"Monto: ${monto:.2f}, Hora: {hora}:00, Frec: {frecuencia}, Ubic: {ubicacion}\n")

    def update_graph(self):
        self.ax.clear()
        labels = list(self.risk_counts.keys())
        counts = list(self.risk_counts.values())
        colors = ['lightgreen', 'gold', 'tomato']
        
        self.ax.bar(labels, counts, color=colors)
        self.ax.set_title("Transacciones por Nivel de Riesgo")
        self.ax.set_ylabel("Cantidad")
        # Asegurar que el eje y sean números enteros
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = FraudDetectorApp(root)
    root.mainloop()
