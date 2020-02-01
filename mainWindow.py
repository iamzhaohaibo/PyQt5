from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
    # 创建一个实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    w.resize(800, 494.4)
    w.move(300, 300)
    w.setWindowTitle('第一个桌面应用')
    w.show()
    sys.exit(app.exec_())
