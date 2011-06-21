'''


Created on 21.06.2011
'''
import sys
from PyQt4 import QtCore, QtGui, QtWebKit

default_url = "http://google.com/"

class BrowserTab(QtGui.QWidget):
    def __init__(self, url=default_url, parent=None):
        super(BrowserTab, self).__init__(parent)

        self.centralwidget = QtGui.QWidget(self)
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        #self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)

        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.gridLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.tb_url = QtGui.QLineEdit()
        self.bt_back = QtGui.QPushButton()
        self.bt_ahead = QtGui.QPushButton()

        self.bt_back.setText("<")
        self.bt_ahead.setText(">")
        #self.bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
        #self.bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))

        self.horizontalLayout.addWidget(self.bt_back)
        self.horizontalLayout.addWidget(self.bt_ahead)
        self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()

        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        self.connect(self.bt_back, QtCore.SIGNAL("clicked()"), self.html.back)
        self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.html.forward)

        self.tb_url.setText(url)
        self.browse()

        mainLayout2 = QtGui.QVBoxLayout()
        mainLayout2.addWidget(self.centralwidget)
        mainLayout2.addWidget(self.html)
        mainLayout2.addStretch(1)
        self.setLayout(mainLayout2)

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        if not url.startsWith("http://"):
            url.insert(0, "http://")
            self.tb_url.setText(url)
        
        self.html.load(QtCore.QUrl(url))
        self.html.show()

class EmptyTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(EmptyTab, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("Empty tab")
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(810,600)
        self.centralwidget = QtGui.QWidget(self)

        tabbedPane = QtGui.QTabWidget(self.centralwidget)
        tabbedPane.addTab(BrowserTab(), "BrowserTab")
        tabbedPane.addTab(EmptyTab(), "EmptyTab")
        self.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
