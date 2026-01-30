from PyQt6.QtWidgets import QMainWindow, QToolBar, QLineEdit, QVBoxLayout, QWidget, QTabWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
name = input("Enter your name: ") # Определяем имя профиля
print("Hello " + name + "!")
if name == "root": # Для красоты
    breakpoint()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Floppa browers")
        self.resize(1024, 768)

        # Создаем панель вкладок
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.setTabsClosable(True)
        self.setCentralWidget(self.tabs)

        # Навигационная панель
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        nav_bar.addAction("Back", lambda: self.tabs.currentWidget().back())
        nav_bar.addAction("Forward", lambda: self.tabs.currentWidget().forward())
        nav_bar.addAction("Reload", lambda: self.tabs.currentWidget().reload())
        nav_bar.addAction("/", lambda: self.tabs.currentWidget().colorCount())
        nav_bar.addWidget(self.url_bar)
        nav_bar.addAction(name, lambda: self.tabs.currentWidget().back())

        # Открываем начальную вкладку
        self.add_new_tab(QUrl("https://github.com/Floppa-os/Floppa-browers.git"), "Mickredset")

    def add_new_tab(self, qurl=None, label="Blank"):
        if qurl is None:
            qurl = QUrl("")

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # Обновление адресной строки при изменении URL в браузере
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url_bar(qurl, browser))

        # Обновление заголовка вкладки
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)

    def update_url_bar(self, q, browser=None):
        if browser == self.tabs.currentWidget():
            self.url_bar.setText(q.toString())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)