import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Task Week 3 - (F1D022137 - MUH. RESSA A.M.)")

        self.label = Gerak("x: 0, y: 0", self)
        self.label.setGeometry(50, 50, 150, 35)

        self.show()
    
    def mouseMoveEvent(self, e):
        self.label.setText(f"x: {e.x()}, y: {e.y()}")

class Gerak(QLabel):
    def __init__(self, teks, induk):
        super().__init__(teks, induk)
        self.induk = induk

    def enterEvent(self, e):
        self.pindah()

    def pindah(self):
        max_x = self.induk.width() - self.width()
        max_y = self.induk.height() - self.height()
        x_baru = random.randint(0, max_x)
        y_baru = random.randint(0, max_y)
        self.move(x_baru, y_baru)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.setMouseTracking(True)
    sys.exit(app.exec_())
