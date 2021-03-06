# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 400)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 340))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 7, 1133, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.analyzerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.analyzerHorizontalLayout.setObjectName("analyzerHorizontalLayout")
        self.graphWidget = PlotWidget(self.verticalLayoutWidget)
        self.graphWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.graphWidget.setObjectName("graphWidget")
        self.analyzerHorizontalLayout.addWidget(self.graphWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parametersHorizontalLayout = QtWidgets.QHBoxLayout()
        self.parametersHorizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.parametersHorizontalLayout.setObjectName("parametersHorizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.analyzerTab = QtWidgets.QWidget()
        self.analyzerTab.setObjectName("analyzerTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.analyzerTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.analyzerInputHorizontalLayout = QtWidgets.QHBoxLayout()
        self.analyzerInputHorizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.analyzerInputHorizontalLayout.setSpacing(10)
        self.analyzerInputHorizontalLayout.setObjectName("analyzerInputHorizontalLayout")
        self.analyzerComboBox = QtWidgets.QComboBox(self.analyzerTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyzerComboBox.sizePolicy().hasHeightForWidth())
        self.analyzerComboBox.setSizePolicy(sizePolicy)
        self.analyzerComboBox.setObjectName("analyzerComboBox")
        self.analyzerInputHorizontalLayout.addWidget(self.analyzerComboBox)
        self.analyzerConnectButton = QtWidgets.QPushButton(self.analyzerTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.analyzerConnectButton.setFont(font)
        self.analyzerConnectButton.setObjectName("analyzerConnectButton")
        self.analyzerInputHorizontalLayout.addWidget(self.analyzerConnectButton)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.analyzerInputHorizontalLayout.addItem(spacerItem)
        self.analyzerLineEdit = QtWidgets.QLineEdit(self.analyzerTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyzerLineEdit.sizePolicy().hasHeightForWidth())
        self.analyzerLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.analyzerLineEdit.setFont(font)
        self.analyzerLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.analyzerLineEdit.setObjectName("analyzerLineEdit")
        self.analyzerInputHorizontalLayout.addWidget(self.analyzerLineEdit)
        self.verticalLayout_5.addLayout(self.analyzerInputHorizontalLayout)
        self.analyzerParamHorizontalLayout = QtWidgets.QHBoxLayout()
        self.analyzerParamHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.analyzerParamHorizontalLayout.setContentsMargins(10, -1, 10, 0)
        self.analyzerParamHorizontalLayout.setSpacing(20)
        self.analyzerParamHorizontalLayout.setObjectName("analyzerParamHorizontalLayout")
        self.analyzatorGridLayout = QtWidgets.QGridLayout()
        self.analyzatorGridLayout.setVerticalSpacing(0)
        self.analyzatorGridLayout.setObjectName("analyzatorGridLayout")
        self.continuousCheckBox = QtWidgets.QCheckBox(self.analyzerTab)
        self.continuousCheckBox.setObjectName("continuousCheckBox")
        self.analyzatorGridLayout.addWidget(self.continuousCheckBox, 7, 2, 1, 1)
        self.fstepLabel = QtWidgets.QLabel(self.analyzerTab)
        self.fstepLabel.setObjectName("fstepLabel")
        self.analyzatorGridLayout.addWidget(self.fstepLabel, 4, 0, 1, 1)
        self.fstopLineEdit = QtWidgets.QLineEdit(self.analyzerTab)
        self.fstopLineEdit.setObjectName("fstopLineEdit")
        self.analyzatorGridLayout.addWidget(self.fstopLineEdit, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.analyzerTab)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.analyzatorGridLayout.addWidget(self.label_5, 6, 2, 1, 1)
        self.fstepLineEdit = QtWidgets.QLineEdit(self.analyzerTab)
        self.fstepLineEdit.setObjectName("fstepLineEdit")
        self.analyzatorGridLayout.addWidget(self.fstepLineEdit, 4, 2, 1, 1)
        self.fstartLabel = QtWidgets.QLabel(self.analyzerTab)
        self.fstartLabel.setObjectName("fstartLabel")
        self.analyzatorGridLayout.addWidget(self.fstartLabel, 2, 0, 1, 1)
        self.singleCheckBox = QtWidgets.QCheckBox(self.analyzerTab)
        self.singleCheckBox.setObjectName("singleCheckBox_3")
        self.analyzatorGridLayout.addWidget(self.singleCheckBox, 7, 3, 1, 1)
        self.fsetButton = QtWidgets.QPushButton(self.analyzerTab)
        self.fsetButton.setObjectName("fsetButton")
        self.analyzatorGridLayout.addWidget(self.fsetButton, 5, 3, 1, 1)
        self.fbwLabel = QtWidgets.QLabel(self.analyzerTab)
        self.fbwLabel.setObjectName("fbwLabel")
        self.analyzatorGridLayout.addWidget(self.fbwLabel, 5, 0, 1, 1)
        self.fbwLineEdit = QtWidgets.QLineEdit(self.analyzerTab)
        self.fbwLineEdit.setObjectName("fbwLineEdit")
        self.analyzatorGridLayout.addWidget(self.fbwLineEdit, 5, 2, 1, 1)
        self.fstopLabel = QtWidgets.QLabel(self.analyzerTab)
        self.fstopLabel.setObjectName("fstopLabel")
        self.analyzatorGridLayout.addWidget(self.fstopLabel, 3, 0, 1, 1)
        self.fstartLineEdit = QtWidgets.QLineEdit(self.analyzerTab)
        self.fstartLineEdit.setObjectName("fstartLineEdit")
        self.analyzatorGridLayout.addWidget(self.fstartLineEdit, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.analyzerTab)
        self.label_2.setObjectName("label_2")
        self.analyzatorGridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.analyzerParamHorizontalLayout.addLayout(self.analyzatorGridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(500, 120, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.analyzerParamHorizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.analyzerParamHorizontalLayout)
        self.tabWidget.addTab(self.analyzerTab, "")
        self.generatorTab = QtWidgets.QWidget()
        self.generatorTab.setObjectName("generatorTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.generatorTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.generatorInputHorizontalLayout = QtWidgets.QHBoxLayout()
        self.generatorInputHorizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.generatorInputHorizontalLayout.setSpacing(10)
        self.generatorInputHorizontalLayout.setObjectName("generatorInputHorizontalLayout")
        self.generatorComboBox = QtWidgets.QComboBox(self.generatorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generatorComboBox.sizePolicy().hasHeightForWidth())
        self.generatorComboBox.setSizePolicy(sizePolicy)
        self.generatorComboBox.setObjectName("generatorComboBox")
        self.generatorInputHorizontalLayout.addWidget(self.generatorComboBox)
        self.generatorConnectButton = QtWidgets.QPushButton(self.generatorTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generatorConnectButton.setFont(font)
        self.generatorConnectButton.setObjectName("generatorConnectButton")
        self.generatorInputHorizontalLayout.addWidget(self.generatorConnectButton)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.generatorInputHorizontalLayout.addItem(spacerItem2)
        self.generatorLineEdit = QtWidgets.QLineEdit(self.generatorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generatorLineEdit.sizePolicy().hasHeightForWidth())
        self.generatorLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.generatorLineEdit.setFont(font)
        self.generatorLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.generatorLineEdit.setObjectName("generatorLineEdit")
        self.generatorInputHorizontalLayout.addWidget(self.generatorLineEdit)
        self.verticalLayout_4.addLayout(self.generatorInputHorizontalLayout)
        self.generatorParamHorizontalLayout = QtWidgets.QHBoxLayout()
        self.generatorParamHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.generatorParamHorizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.generatorParamHorizontalLayout.setSpacing(10)
        self.generatorParamHorizontalLayout.setObjectName("generatorParamHorizontalLayout")
        self.generatorGridLayout = QtWidgets.QGridLayout()
        self.generatorGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.generatorGridLayout.setContentsMargins(-1, 0, -1, 0)
        self.generatorGridLayout.setHorizontalSpacing(3)
        self.generatorGridLayout.setVerticalSpacing(0)
        self.generatorGridLayout.setObjectName("generatorGridLayout")
        self.label_7 = QtWidgets.QLabel(self.generatorTab)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.generatorGridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.freqLabel = QtWidgets.QLabel(self.generatorTab)
        self.freqLabel.setObjectName("freqLabel")
        self.generatorGridLayout.addWidget(self.freqLabel, 3, 0, 1, 1)
        self.powerLabel = QtWidgets.QLabel(self.generatorTab)
        self.powerLabel.setObjectName("powerLabel")
        self.generatorGridLayout.addWidget(self.powerLabel, 2, 0, 1, 1)
        self.genFreqLineEdit = QtWidgets.QLineEdit(self.generatorTab)
        self.genFreqLineEdit.setObjectName("genFreqLineEdit")
        self.generatorGridLayout.addWidget(self.genFreqLineEdit, 3, 1, 1, 1)
        self.genPowerLineEdit = QtWidgets.QLineEdit(self.generatorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genPowerLineEdit.sizePolicy().hasHeightForWidth())
        self.genPowerLineEdit.setSizePolicy(sizePolicy)
        self.genPowerLineEdit.setObjectName("genPowerLineEdit")
        self.generatorGridLayout.addWidget(self.genPowerLineEdit, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.generatorTab)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.generatorGridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.psweepCheckBox = QtWidgets.QCheckBox(self.generatorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.psweepCheckBox.sizePolicy().hasHeightForWidth())
        self.psweepCheckBox.setSizePolicy(sizePolicy)
        self.psweepCheckBox.setMinimumSize(QtCore.QSize(0, 20))
        self.psweepCheckBox.setObjectName("psweepCheckBox")
        self.generatorGridLayout.addWidget(self.psweepCheckBox, 7, 2, 1, 1)
        self.genFreqButton = QtWidgets.QPushButton(self.generatorTab)
        self.genFreqButton.setObjectName("genFreqButton")
        self.generatorGridLayout.addWidget(self.genFreqButton, 3, 2, 1, 1)
        self.genPowerButton = QtWidgets.QPushButton(self.generatorTab)
        self.genPowerButton.setObjectName("genPowerButton")
        self.generatorGridLayout.addWidget(self.genPowerButton, 2, 2, 1, 1)
        self.fsweepCheckBox = QtWidgets.QCheckBox(self.generatorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fsweepCheckBox.sizePolicy().hasHeightForWidth())
        self.fsweepCheckBox.setSizePolicy(sizePolicy)
        self.fsweepCheckBox.setMinimumSize(QtCore.QSize(0, 20))
        self.fsweepCheckBox.setObjectName("fsweepCheckBox")
        self.generatorGridLayout.addWidget(self.fsweepCheckBox, 7, 1, 1, 1)
        self.genOnButton = QtWidgets.QPushButton(self.generatorTab)
        self.genOnButton.setObjectName("genOnButton")
        self.generatorGridLayout.addWidget(self.genOnButton, 8, 1, 1, 2)
        self.generatorParamHorizontalLayout.addLayout(self.generatorGridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.generatorParamHorizontalLayout.addItem(spacerItem3)
        self.psweepGridLayout = QtWidgets.QGridLayout()
        self.psweepGridLayout.setHorizontalSpacing(3)
        self.psweepGridLayout.setVerticalSpacing(0)
        self.psweepGridLayout.setObjectName("psweepGridLayout")
        self.fstartLabel_2 = QtWidgets.QLabel(self.generatorTab)
        self.fstartLabel_2.setObjectName("fstartLabel_2")
        self.psweepGridLayout.addWidget(self.fstartLabel_2, 1, 0, 1, 1)
        self.fstopLabel_2 = QtWidgets.QLabel(self.generatorTab)
        self.fstopLabel_2.setObjectName("fstopLabel_2")
        self.psweepGridLayout.addWidget(self.fstopLabel_2, 2, 0, 1, 1)
        self.fbwLabel_2 = QtWidgets.QLabel(self.generatorTab)
        self.fbwLabel_2.setObjectName("fbwLabel_2")
        self.psweepGridLayout.addWidget(self.fbwLabel_2, 4, 0, 1, 1)
        self.fstepLineEdit_2 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstepLineEdit_2.setObjectName("fstepLineEdit_2")
        self.psweepGridLayout.addWidget(self.fstepLineEdit_2, 3, 2, 1, 1)
        self.fbwLineEdit_2 = QtWidgets.QLineEdit(self.generatorTab)
        self.fbwLineEdit_2.setObjectName("fbwLineEdit_2")
        self.psweepGridLayout.addWidget(self.fbwLineEdit_2, 4, 2, 1, 1)
        self.fstopLineEdit_2 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstopLineEdit_2.setObjectName("fstopLineEdit_2")
        self.psweepGridLayout.addWidget(self.fstopLineEdit_2, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.generatorTab)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.psweepGridLayout.addWidget(self.label_4, 0, 2, 1, 2)
        self.fstepLabel_2 = QtWidgets.QLabel(self.generatorTab)
        self.fstepLabel_2.setObjectName("fstepLabel_2")
        self.psweepGridLayout.addWidget(self.fstepLabel_2, 3, 0, 1, 1)
        self.fstartLineEdit_2 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstartLineEdit_2.setEnabled(True)
        self.fstartLineEdit_2.setObjectName("fstartLineEdit_2")
        self.psweepGridLayout.addWidget(self.fstartLineEdit_2, 1, 2, 1, 1)
        self.fsetButton_2 = QtWidgets.QPushButton(self.generatorTab)
        self.fsetButton_2.setObjectName("fsetButton_2")
        self.psweepGridLayout.addWidget(self.fsetButton_2, 4, 3, 1, 1)
        self.generatorParamHorizontalLayout.addLayout(self.psweepGridLayout)
        self.fsweepGridLayout = QtWidgets.QGridLayout()
        self.fsweepGridLayout.setContentsMargins(0, -1, -1, -1)
        self.fsweepGridLayout.setHorizontalSpacing(3)
        self.fsweepGridLayout.setVerticalSpacing(0)
        self.fsweepGridLayout.setObjectName("fsweepGridLayout")
        self.fstopLineEdit_3 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstopLineEdit_3.setObjectName("fstopLineEdit_3")
        self.fsweepGridLayout.addWidget(self.fstopLineEdit_3, 2, 2, 1, 1)
        self.fstartLineEdit_3 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstartLineEdit_3.setObjectName("fstartLineEdit_3")
        self.fsweepGridLayout.addWidget(self.fstartLineEdit_3, 1, 2, 1, 1)
        self.fbwLineEdit_3 = QtWidgets.QLineEdit(self.generatorTab)
        self.fbwLineEdit_3.setObjectName("fbwLineEdit_3")
        self.fsweepGridLayout.addWidget(self.fbwLineEdit_3, 4, 2, 1, 1)
        self.fstepLineEdit_3 = QtWidgets.QLineEdit(self.generatorTab)
        self.fstepLineEdit_3.setObjectName("fstepLineEdit_3")
        self.fsweepGridLayout.addWidget(self.fstepLineEdit_3, 3, 2, 1, 1)
        self.fsetButton_3 = QtWidgets.QPushButton(self.generatorTab)
        self.fsetButton_3.setObjectName("fsetButton_3")
        self.fsweepGridLayout.addWidget(self.fsetButton_3, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.generatorTab)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.fsweepGridLayout.addWidget(self.label_3, 0, 2, 1, 2)
        self.fstartLabel_3 = QtWidgets.QLabel(self.generatorTab)
        self.fstartLabel_3.setObjectName("fstartLabel_3")
        self.fsweepGridLayout.addWidget(self.fstartLabel_3, 1, 0, 1, 2)
        self.fstopLabel_3 = QtWidgets.QLabel(self.generatorTab)
        self.fstopLabel_3.setObjectName("fstopLabel_3")
        self.fsweepGridLayout.addWidget(self.fstopLabel_3, 2, 0, 1, 2)
        self.fstepLabel_3 = QtWidgets.QLabel(self.generatorTab)
        self.fstepLabel_3.setObjectName("fstepLabel_3")
        self.fsweepGridLayout.addWidget(self.fstepLabel_3, 3, 0, 1, 2)
        self.fbwLabel_3 = QtWidgets.QLabel(self.generatorTab)
        self.fbwLabel_3.setObjectName("fbwLabel_3")
        self.fsweepGridLayout.addWidget(self.fbwLabel_3, 4, 0, 1, 2)
        self.generatorParamHorizontalLayout.addLayout(self.fsweepGridLayout)
        self.verticalLayout_4.addLayout(self.generatorParamHorizontalLayout)
        self.tabWidget.addTab(self.generatorTab, "")
        self.parametersHorizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.parametersHorizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setContentsMargins(20, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dbLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dbLabel.setObjectName("dbLabel")
        self.gridLayout_2.addWidget(self.dbLabel, 3, 0, 1, 1)
        self.refLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.refLabel.setObjectName("refLabel")
        self.gridLayout_2.addWidget(self.refLabel, 2, 0, 1, 1)
        self.dbLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dbLineEdit.setObjectName("dbLineEdit")
        self.gridLayout_2.addWidget(self.dbLineEdit, 3, 1, 1, 1)
        self.refLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.refLineEdit.setObjectName("refLineEdit")
        self.gridLayout_2.addWidget(self.refLineEdit, 2, 1, 1, 1)
        self.dbButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dbButton.setObjectName("dbButton")
        self.gridLayout_2.addWidget(self.dbButton, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 3, 1, 1)
        self.refButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.refButton.setObjectName("refButton")
        self.gridLayout_2.addWidget(self.refButton, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.analyzerHorizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.analyzerHorizontalLayout)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.analyzerConnectButton.setText(_translate("MainWindow", "CONNECT"))
        self.continuousCheckBox.setText(_translate("MainWindow", "Continuous"))
        self.fstepLabel.setText(_translate("MainWindow", "step"))
        self.fstartLabel.setText(_translate("MainWindow", "start"))
        self.singleCheckBox.setText(_translate("MainWindow", "Single"))
        self.fsetButton.setText(_translate("MainWindow", "SET"))
        self.fbwLabel.setText(_translate("MainWindow", "bw"))
        self.fstopLabel.setText(_translate("MainWindow", "stop"))
        self.label_2.setText(_translate("MainWindow", "Frequency:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyzerTab), _translate("MainWindow", "Spectrum Analyzer"))
        self.generatorConnectButton.setText(_translate("MainWindow", "CONNECT"))
        self.freqLabel.setText(_translate("MainWindow", "Frequency"))
        self.powerLabel.setText(_translate("MainWindow", "Power"))
        self.psweepCheckBox.setText(_translate("MainWindow", "Power sweep"))
        self.genFreqButton.setText(_translate("MainWindow", "SET"))
        self.genPowerButton.setText(_translate("MainWindow", "SET"))
        self.fsweepCheckBox.setText(_translate("MainWindow", "Freq sweep"))
        self.genOnButton.setText(_translate("MainWindow", "ON"))
        self.fstartLabel_2.setText(_translate("MainWindow", "start"))
        self.fstopLabel_2.setText(_translate("MainWindow", "stop"))
        self.fbwLabel_2.setText(_translate("MainWindow", "bw"))
        self.label_4.setText(_translate("MainWindow", "FREQUENCY SWEEP"))
        self.fstepLabel_2.setText(_translate("MainWindow", "step"))
        self.fsetButton_2.setText(_translate("MainWindow", "SET"))
        self.fsetButton_3.setText(_translate("MainWindow", "SET"))
        self.label_3.setText(_translate("MainWindow", "POWER SWEEP"))
        self.fstartLabel_3.setText(_translate("MainWindow", "start"))
        self.fstopLabel_3.setText(_translate("MainWindow", "stop"))
        self.fstepLabel_3.setText(_translate("MainWindow", "step"))
        self.fbwLabel_3.setText(_translate("MainWindow", "bw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generatorTab), _translate("MainWindow", "Signal Generator"))
        self.dbLabel.setText(_translate("MainWindow", "dB/div"))
        self.refLabel.setText(_translate("MainWindow", "Ref level"))
        self.dbButton.setText(_translate("MainWindow", "SET"))
        self.label.setText(_translate("MainWindow", "Chart parameters"))
        self.refButton.setText(_translate("MainWindow", "SET"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

