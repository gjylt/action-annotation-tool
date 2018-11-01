from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_TabWidget(object):
    def setupUi(self, TabWidget):

        TabWidget.setObjectName("TabWidget") #创建的是"TabWidget"
        TabWidget.resize(789, 619)
        #TabWidget.setScaledContents(True)


        self.lef_side   = 75
        self.right_side = 75


        self.main_w = self.size().width()
        self.main_h = self.size().height()

        # "第一个子窗口"
        self.tab = QtWidgets.QWidget()

        self.tab.setObjectName("tab")

        self.pushButton = QtWidgets.QPushButton(TabWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_4 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_h_ration = 0.8
        self.label_w_ration = 0.8
        lab_h = int(self.main_h*self.label_h_ration)
        lab_w = int(self.label_w_ration*self.main_w)
        self.label = QtWidgets.QLabel(TabWidget)
        self.label.setGeometry(QtCore.QRect(110, 30, lab_w, lab_h ))
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setObjectName("label")


        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, TabWidget)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setSingleStep(1)
        self.slider.setGeometry(110, lab_h +40, lab_w, 30)




        #TabWidget.addTab(self.tab, "")


        self.retranslateUi(TabWidget)

        TabWidget.setCurrentIndex(0)


        # 将按键与事件相连
        self.pushButton.clicked.connect(TabWidget.ReplayVideo)
        self.pushButton_2.clicked.connect(TabWidget.videoprocessing)
        self.pushButton_3.clicked.connect(TabWidget.saverannotation)
        self.pushButton_4.clicked.connect(TabWidget.setsavepath)

        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.pushButton.setText(_translate("TabWidget", "重新播放"))
        self.pushButton_2.setText(_translate("TabWidget", "打开视频"))
        self.pushButton_3.setText(_translate("TabWidget", "保存标签"))
        self.pushButton_4.setText(_translate("TabWidget", "标签路径"))

        #TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))

        # TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))
        # TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "页"))

