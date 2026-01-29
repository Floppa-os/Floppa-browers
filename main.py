import sys
from PyQt6.QtWidgets import QApplication
from browser_window import MainWindow
print("import QWebEngineView")
print("import sys")
print("from PyQt6.QtWidgets import QApplication")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()