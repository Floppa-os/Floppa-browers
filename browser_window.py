from PyQt6.QtWidgets import QMainWindow, QToolBar, QLineEdit, QVBoxLayout, QWidget, QTabWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
name = input("Enter your name: ") # Определяем имя профиля
print("Hello " + name + "!")
if name == "root": # Для красоты
    breakpoint()
print("https://github.com/Floppa-os/Floppa-browers/blob/main/README.md")
print("run - run")
print("breakpoint - break")
run = input(name + " >")
if run == "run":
    print("Hello " + name + "!")
if run == "break":
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
        self.tabs.currentChanged.connect(self.navigate_to_url)

        # Навигационная панель
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)
        print("nav_bar = QToolBar()")

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        nav_bar.addAction("Back", lambda: self.tabs.currentWidget().back())
        nav_bar.addAction("Forward", lambda: self.tabs.currentWidget().forward())
        nav_bar.addAction("Reload", lambda: self.tabs.currentWidget().reload())
        nav_bar.addAction("/", lambda: self.tabs.currentWidget().colorCount())
        nav_bar.addWidget(self.url_bar)
        nav_bar.addAction(name, lambda: self.tabs.currentWidget().back())

        # Открываем начальную вкладку
        self.add_new_tab(QUrl("https://sun9-59.userapi.com/s/v1/ig2/v3qpJtCi8-0cWteEXcRT3LT5eXn-d5DyRXypf9lqZE2oUnDfUGhVAKFVhKLnoCXuO4OfEI7yu2Xlqf0sEpN-fYYS.jpg?quality=96&as=32x66,48x99,72x148,108x222,160x330,240x494,360x742,480x989,540x1112,640x1318,720x1483,932x1920&from=bu&cs=640x0"), "Mickredset")

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