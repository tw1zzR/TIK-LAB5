from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from methods import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.container = QWidget()

        self.u_min_input = QLineEdit(self)
        self.u_max_input = QLineEdit(self)
        self.samples_input = QLineEdit(self)
        self.duration_input = QLineEdit(self)
        self.h_diff_input = QLineEdit(self)
        self.h_cond_input = QLineEdit(self)

        self.calc_btn = QPushButton("CALCULATE", self)

        self.entropy_result = QLabel("Entropy Result: ")
        self.info_speed_result = QLabel("Information Speed: ")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Entropy/Information Speed Calculator")
        self.setGeometry(1100, 500, 400, 300)
        self.setWindowIcon(QIcon("icon.png"))

        self.u_min_input.setPlaceholderText("Enter U min (mV)")
        self.u_max_input.setPlaceholderText("Enter U max (mV)")
        self.samples_input.setPlaceholderText("Samples count")
        self.duration_input.setPlaceholderText("Message duration (s)")
        self.h_diff_input.setPlaceholderText("Differential entropy (bits/sample)")
        self.h_cond_input.setPlaceholderText("Conditional differential entropy (bits/sample)")

        self.calc_btn.clicked.connect(self.perform_calculations)

        self.layout.addWidget(self.u_min_input)
        self.layout.addWidget(self.u_max_input)
        self.layout.addWidget(self.samples_input)
        self.layout.addWidget(self.duration_input)
        self.layout.addWidget(self.h_diff_input)
        self.layout.addWidget(self.h_cond_input)
        self.layout.addWidget(self.calc_btn)
        self.layout.addWidget(self.entropy_result)
        self.layout.addWidget(self.info_speed_result)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.setStyleSheet("""
                    QLineEdit {
                        font-size: 14px;
                        padding: 6px;
                        border: 2px solid #444;
                        border-radius: 5px;
                        background-color: #ffffff;
                        font-family: Helvetica;
                    }
                    QLabel {
                        font-size: 16px;
                        font-weight: bold;
                        font-family: Helvetica;
                    }
                    QPushButton {
                        font-size: 16px;
                        font-weight: bold;
                        background-color: #3ac45e;
                        border: none;
                        padding: 12px;
                        color: white;
                        font-family: Helvetica;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #34b155;
                    }
                    QWidget {
                        background-color: #d3d7d4;
                        font-family: Helvetica;
                    }
                """)

    def perform_calculations(self):
        try:
            u_min = float(self.u_min_input.text())
            u_max = float(self.u_max_input.text())
            entropy_mv, entropy_uv = calculate_entropy_change(u_min, u_max)
            self.entropy_result.setText(
                f"Entropy (mV): {entropy_mv:.4f} bits | Entropy (uV): {entropy_uv:.4f} bits"
            )
        except ValueError:
            self.entropy_result.setText("Invalid input for U min/max.")

        try:
            samples = int(self.samples_input.text())
            duration = float(self.duration_input.text())
            h_diff = float(self.h_diff_input.text())
            h_cond = float(self.h_cond_input.text())
            info_speed = calculate_average_information_speed(samples, duration, h_diff, h_cond)
            self.info_speed_result.setText(f"Information Speed: {info_speed:.4f} bits/s")
        except ValueError:
            self.info_speed_result.setText("Invalid input for info speed task.")