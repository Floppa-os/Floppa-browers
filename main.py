import random
import sys
from PyQt6.QtWidgets import QApplication
from browser_window import MainWindow
print("import QWebEngineView")
print("import sys")
print("from PyQt6.QtWidgets import QApplication")
id1 = random.randint(125, 255)
id2 = random.randint(125, 136)
id3 = random.randint(3, 13)
id4 = random.randint(456, 499)
id = id1 + id2 + id3 + id4
print(id1)
print(id2)
print(id3)
print(id4)
print(id)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()