import random
import sys
from PyQt6.QtWidgets import QApplication
from browser_window import MainWindow, name
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
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
print("if __name__ == __main__")
print(id)
print("breakpoint - break")
print("run - run")
run = input(name + " >")
if run == "run":
    print("Hello " + name + "!")
if run == "break":
    breakpoint()
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Загрузка файлов")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Файл не выбран")
        layout.addWidget(self.label)

        self.btn = QPushButton("Выбрать файл")
        self.btn.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.btn)

        container = QWidget()
        container.setLayout(layout)
        setCentralWidget(container)

    def open_file_dialog(self):
        # Открывает окно выбора файла
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",
            "Все файлы (*);;Текстовые файлы (*.txt);;Изображения (*.png *.jpg)"
        )

        if file_path:
            self.label.setText(f"Выбран: {file_path}")
            # Здесь можно добавить логику обработки или копирования файла


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())