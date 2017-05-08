# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyreeMainWindow(object):
    def setupUi(self, PyreeMainWindow):
        PyreeMainWindow.setObjectName("PyreeMainWindow")
        PyreeMainWindow.resize(971, 634)
        self.centralwidget = QtWidgets.QWidget(PyreeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        PyreeMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyreeMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        PyreeMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyreeMainWindow)
        self.statusbar.setObjectName("statusbar")
        PyreeMainWindow.setStatusBar(self.statusbar)
        self.workersDockWidget = QtWidgets.QDockWidget(PyreeMainWindow)
        self.workersDockWidget.setObjectName("workersDockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.workersDockWidget.setWidget(self.dockWidgetContents)
        PyreeMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.workersDockWidget)
        self.sheetsDockWidget = QtWidgets.QDockWidget(PyreeMainWindow)
        self.sheetsDockWidget.setObjectName("sheetsDockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSheetPushButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSheetPushButton.sizePolicy().hasHeightForWidth())
        self.addSheetPushButton.setSizePolicy(sizePolicy)
        self.addSheetPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addSheetPushButton.setFlat(False)
        self.addSheetPushButton.setObjectName("addSheetPushButton")
        self.horizontalLayout_2.addWidget(self.addSheetPushButton)
        self.addSheetLineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSheetLineEdit.sizePolicy().hasHeightForWidth())
        self.addSheetLineEdit.setSizePolicy(sizePolicy)
        self.addSheetLineEdit.setObjectName("addSheetLineEdit")
        self.horizontalLayout_2.addWidget(self.addSheetLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sheetListWidget = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.sheetListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.sheetListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.sheetListWidget.setObjectName("sheetListWidget")
        self.verticalLayout.addWidget(self.sheetListWidget)
        self.sheetsDockWidget.setWidget(self.dockWidgetContents_2)
        PyreeMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.sheetsDockWidget)
        self.propertiesDockWidget = QtWidgets.QDockWidget(PyreeMainWindow)
        self.propertiesDockWidget.setObjectName("propertiesDockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.propertiesDockWidget.setWidget(self.dockWidgetContents_3)
        PyreeMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.propertiesDockWidget)
        self.actionOpen = QtWidgets.QAction(PyreeMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PyreeMainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(PyreeMainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew_Project = QtWidgets.QAction(PyreeMainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionExit = QtWidgets.QAction(PyreeMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(PyreeMainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(PyreeMainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionImport_sheet = QtWidgets.QAction(PyreeMainWindow)
        self.actionImport_sheet.setObjectName("actionImport_sheet")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_sheet)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(PyreeMainWindow)
        self.tabWidget.setCurrentIndex(-1)
        self.addSheetLineEdit.returnPressed.connect(self.addSheetPushButton.click)
        QtCore.QMetaObject.connectSlotsByName(PyreeMainWindow)

    def retranslateUi(self, PyreeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PyreeMainWindow.setWindowTitle(_translate("PyreeMainWindow", "PyreeMainWindow"))
        self.menuFile.setTitle(_translate("PyreeMainWindow", "File"))
        self.menuEdit.setTitle(_translate("PyreeMainWindow", "Edit"))
        self.workersDockWidget.setWindowTitle(_translate("PyreeMainWindow", "Workers"))
        self.sheetsDockWidget.setWindowTitle(_translate("PyreeMainWindow", "Sheets"))
        self.addSheetPushButton.setToolTip(_translate("PyreeMainWindow", "Create a new sheet"))
        self.addSheetPushButton.setText(_translate("PyreeMainWindow", "+"))
        self.addSheetLineEdit.setToolTip(_translate("PyreeMainWindow", "Name the new sheet shall have"))
        self.addSheetLineEdit.setPlaceholderText(_translate("PyreeMainWindow", "Name of new sheet"))
        self.propertiesDockWidget.setWindowTitle(_translate("PyreeMainWindow", "Properties"))
        self.actionOpen.setText(_translate("PyreeMainWindow", "Open"))
        self.actionSave.setText(_translate("PyreeMainWindow", "Save"))
        self.actionSave_as.setText(_translate("PyreeMainWindow", "Save as"))
        self.actionNew_Project.setText(_translate("PyreeMainWindow", "New Project"))
        self.actionExit.setText(_translate("PyreeMainWindow", "Exit"))
        self.actionUndo.setText(_translate("PyreeMainWindow", "Undo"))
        self.actionRedo.setText(_translate("PyreeMainWindow", "Redo"))
        self.actionImport_sheet.setText(_translate("PyreeMainWindow", "Import sheet"))

