# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstsample.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1215, 607)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/geo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setAutoFillBackground(False)
        self.tab_9.setStyleSheet("QWidget:hover{\n"
"background-color: white;\n"
"}\n"
"QWidget:selected {\n"
" background-color: black; \n"
"}\n"
"")
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1215, 21))
        self.menubar.setStyleSheet("QMenuBar {\n"
"background:white;\n"
"/*border-bottom: 1px solid black;*/\n"
"    spacing: 3px;\n"
"}\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("QMenu {\n"
"    background-color: #ABABAB; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: darkgray;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"QMenu{\n"
"background-color: white;\n"
"}\n"
"QMenu:selected {\n"
" background-color: gray; \n"
"}\n"
"QMenu:pressed { \n"
"background-color: black;\n"
"}")
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("QMenu {\n"
"    background-color: #ABABAB; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"QMenu{\n"
"background-color: white;\n"
"}\n"
"QMenu:selected {\n"
" background-color: gray; \n"
"}\n"
"QMenu:pressed { \n"
"background-color: black;\n"
"}")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Database = QtWidgets.QAction(MainWindow)
        self.actionOpen_Database.setObjectName("actionOpen_Database")
        self.actionClose_Database = QtWidgets.QAction(MainWindow)
        self.actionClose_Database.setObjectName("actionClose_Database")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionOur_site = QtWidgets.QAction(MainWindow)
        self.actionOur_site.setObjectName("actionOur_site")
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addAction(self.actionClose_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionOur_site)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GEOMETR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Страница"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Страница"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Страница"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Database.setText(_translate("MainWindow", "Open Database"))
        self.actionClose_Database.setText(_translate("MainWindow", "Close Database"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionOur_site.setText(_translate("MainWindow", "Our site"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
