import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

SCREEN_SIZE = [600, 600]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.y = '0'
        self.x = '0'
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.y},{self.x}&spn=0.002,0.002&l=map"
        response = requests.get(map_request)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.update()

    def update(self):
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(750, 250, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        self.coordsx = QLineEdit(self)
        self.coordsx.move(50, 500)
        self.coordsx.resize(200, 50)
        self.coordsy = QLineEdit(self)
        self.coordsy.move(300, 500)
        self.coordsy.resize(200, 50)
        self.label_x = QLabel('Координаты X', self)
        self.label_x.move(80, 480)
        self.label_y = QLabel('Координаты Y', self)
        self.label_y.move(330, 480)
        self.btn_start = QPushButton('Start', self)
        self.btn_start.move(230, 560)
        self.btn_start.clicked.connect(self.render)

    def render(self):
        self.x = self.coordsx.text()
        self.y = self.coordsy.text()
        self.pixmap = None
        self.getImage()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
