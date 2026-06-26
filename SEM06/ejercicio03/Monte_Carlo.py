import sys
import random
import math

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setWindowTitle("Simulador Monte Carlo para PI")
        MainWindow.resize(900, 700)

        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.lblTitulo = QLabel("Cantidad de simulaciones:", self.centralwidget)
        self.lblTitulo.setGeometry(20, 20, 180, 30)

        self.txtSimulaciones = QLineEdit(self.centralwidget)
        self.txtSimulaciones.setGeometry(200, 20, 120, 30)
        self.txtSimulaciones.setText("1000")

        self.btnSimular = QPushButton("Ejecutar Simulación", self.centralwidget)
        self.btnSimular.setGeometry(340, 20, 180, 30)

        self.lblPi = QLabel("π estimado:", self.centralwidget)
        self.lblPi.setGeometry(20, 70, 500, 30)

        self.lblError = QLabel("Error porcentual:", self.centralwidget)
        self.lblError.setGeometry(20, 100, 500, 30)

        self.widgetGrafica = QWidget(self.centralwidget)
        self.widgetGrafica.setGeometry(20, 150, 850, 500)

        self.layoutGrafica = QVBoxLayout(self.widgetGrafica)


class Ventana(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figura = Figure()
        self.canvas = FigureCanvas(self.figura)

        self.ui.layoutGrafica.addWidget(self.canvas)

        self.ui.btnSimular.clicked.connect(self.simular)

    def simular(self):

        try:

            simulaciones = int(self.ui.txtSimulaciones.text())

            if simulaciones <= 0:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Ingrese un número mayor que cero"
                )
                return

            dentro = 0

            x_dentro = []
            y_dentro = []

            x_fuera = []
            y_fuera = []

            for i in range(simulaciones):

                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)

                if x**2 + y**2 <= 1:

                    dentro += 1

                    x_dentro.append(x)
                    y_dentro.append(y)

                else:

                    x_fuera.append(x)
                    y_fuera.append(y)

            pi_estimado = 4 * dentro / simulaciones

            error = (
                abs(math.pi - pi_estimado)
                / math.pi
                * 100
            )

            self.ui.lblPi.setText(
                f"π estimado: {pi_estimado:.6f}"
            )

            self.ui.lblError.setText(
                f"Error porcentual: {error:.4f}%"
            )

            self.graficar(
                x_dentro,
                y_dentro,
                x_fuera,
                y_fuera
            )

        except ValueError:

            QMessageBox.warning(
                self,
                "Error",
                "Ingrese un número válido"
            )

    def graficar(
        self,
        x_dentro,
        y_dentro,
        x_fuera,
        y_fuera
    ):

        self.figura.clear()

        ax = self.figura.add_subplot(111)

        ax.scatter(
            x_dentro,
            y_dentro,
            s=5,
            label="Dentro de la circunferencia"
        )

        ax.scatter(
            x_fuera,
            y_fuera,
            s=5,
            label="Fuera de la circunferencia"
        )

        ax.set_title(
            "Estimación de PI mediante Monte Carlo"
        )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        ax.legend()

        ax.grid(True)

        self.canvas.draw()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec_())