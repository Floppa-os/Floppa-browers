from PyQt6.QtWebEngineCore import QWebEngineProfile

def setup_browser_profile():
    # Настройка стандартного профиля (например, для управления куками или кэшем)
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) PythonBrowser/1.0")
    return profile