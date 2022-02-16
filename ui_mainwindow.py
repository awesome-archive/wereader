# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 704)
        MainWindow.setBaseSize(QtCore.QSize(1080, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.browser = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setBaseSize(QtCore.QSize(1080, 700))
        self.browser.setAutoFillBackground(True)
        self.browser.setObjectName("browser")
        self.splitter_2 = QtWidgets.QSplitter(self.browser)
        self.splitter_2.setGeometry(QtCore.QRect(5, 0, 1070, 700))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.listView = QtWidgets.QListView(self.splitter)
        self.listView.setObjectName("listView")
        self.tableView = QtWidgets.QTableView(self.splitter)
        self.tableView.setObjectName("tableView")
        self.noteEdit = QtWidgets.QTextEdit(self.splitter_2)
        self.noteEdit.setObjectName("noteEdit")
        MainWindow.setCentralWidget(self.browser)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 23))
        self.menubar.setObjectName("menubar")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuNote = QtWidgets.QMenu(self.menubar)
        self.menuNote.setObjectName("menuNote")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionLoadNotes = QtWidgets.QAction(MainWindow)
        self.actionLoadNotes.setObjectName("actionLoadNotes")
        self.actionShow = QtWidgets.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionLoadShelf = QtWidgets.QAction(MainWindow)
        self.actionLoadShelf.setObjectName("actionLoadShelf")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionHide = QtWidgets.QAction(MainWindow)
        self.actionHide.setObjectName("actionHide")
        self.actionLoadHot = QtWidgets.QAction(MainWindow)
        self.actionLoadHot.setObjectName("actionLoadHot")
        self.menuTool.addAction(self.actionLoadShelf)
        self.menuTool.addAction(self.actionLoadNotes)
        self.menuNote.addSeparator()
        self.menuNote.addAction(self.actionShow)
        self.menuNote.addAction(self.actionSave)
        self.menuNote.addSeparator()
        self.menuNote.addAction(self.actionLoadHot)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.actionLicense)
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuNote.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信读书助手-wereader"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuNote.setTitle(_translate("MainWindow", "Note"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLoadNotes.setText(_translate("MainWindow", "下载全部笔记"))
        self.actionShow.setText(_translate("MainWindow", "切换笔记模式"))
        self.actionShow.setShortcut(_translate("MainWindow", "Ctrl+Tab"))
        self.actionSave.setText(_translate("MainWindow", "保存笔记"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAuthor.setText(_translate("MainWindow", "Author <arry_lee@qq.com>"))
        self.actionAuthor.setToolTip(_translate("MainWindow", "Author"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionLoadShelf.setText(_translate("MainWindow", "加载书架"))
        self.actionLoadShelf.setToolTip(_translate("MainWindow", "Download shelf"))
        self.actionOpen.setText(_translate("MainWindow", "打开"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionHide.setText(_translate("MainWindow", "Hide"))
        self.actionLoadHot.setText(_translate("MainWindow", "热门笔记"))
