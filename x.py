from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):

        TabWidget.setObjectName("TabWidget") #创建的是"TabWidget"
        TabWidget.resize(789, 619)

        #############################################
        self.lef_side = 110
        self.right_side = 110
        self.top_side = 30
        self.bottom_side = 30
        self.slider_height = 30
        self.button_width = 75
        self.button_height = 23
        self.slider_label_blank = 5

        self.main_w = self.size().width()
        self.main_h = self.size().height()

        # button
        self.button_x = 10

        # label
        self.label_x = self.lef_side
        self.label_y = self.top_side
        self.label_width = self.main_w - self.lef_side - self.right_side
        self.label_height = self.main_h - self.slider_height - self.slider_label_blank

        # slider
        self.slider_x = self.lef_side
        self.slider_y = self.main_h - self.bottom_side - self.slider_height
        self.slider_width = self.label_width

        ################################




        # "第一个子窗口"
        # self.tab = QtWidgets.QWidget()
        #
        # self.tab.setObjectName("tab")

        #list widget
        self.list = QtWidgets.QListWidget(TabWidget)
        self.setFocusPolicy(QtCore.Qt.NoFocus)


        self.pushButton = QtWidgets.QPushButton(TabWidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(TabWidget)
        self.pushButton_6.setObjectName("pushButton_6")

        self.label = QtWidgets.QLabel(TabWidget)
        #self.label.setGeometry(QtCore.QRect(self.label_x, self.label_y, self.label_width, self.label_height))
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setObjectName("label")

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, TabWidget)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setSingleStep(1)
        #self.slider.setGeometry(self.slider_x, self.slider_y, self.slider_width, self.slider_height)



        #self.recalc_layout(self)


        self.retranslateUi(TabWidget)

        TabWidget.setCurrentIndex(0)


        # 将按键与事件相连
        self.pushButton.clicked.connect(TabWidget.ReplayVideo)
        self.pushButton_2.clicked.connect(TabWidget.videoprocessing)
        self.pushButton_3.clicked.connect(TabWidget.saverannotation)
        self.pushButton_4.clicked.connect(TabWidget.setsavepath)
        self.pushButton_5.clicked.connect(TabWidget.VideoPlayPause)
        self.pushButton_6.clicked.connect(TabWidget.SetVideoDri)

        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def recalc_layout(self, TabWidget):
        ############################

        self.lef_side    = 110
        self.right_side  = 200
        self.top_side    = 30
        self.bottom_side = 30
        self.slider_height    = 30
        self.button_width = 75
        self.button_height = 23
        self.slider_label_blank = 5

        self.main_w      = self.size().width()
        self.main_h      = self.size().height()

        #button
        self.button_x = 10

        #label
        self.label_x = self.lef_side
        self.label_y = self.top_side
        self.label_width = self.main_w - self.lef_side - self.right_side
        self.label_height= self.main_h - self.slider_height - self.slider_label_blank - self.top_side - self.bottom_side

        #slider
        self.slider_x = self.lef_side
        self.slider_y = self.main_h - self.bottom_side - self.slider_height
        self.slider_width = self.label_width

        #list
        self.list_x = self.lef_side + self.label_width + 9
        self.list_y = self.top_side
        self.list_width = self.right_side-20
        self.list_height= int(self.label_height*0.8)

        ################################

        self.pushButton.setGeometry(QtCore.QRect(self.button_x, 30, self.button_width, self.button_height))

        self.pushButton_2.setGeometry(QtCore.QRect(self.button_x, 90, self.button_width, self.button_height))

        self.pushButton_3.setGeometry(QtCore.QRect(self.button_x, 150, self.button_width, self.button_height))

        self.pushButton_4.setGeometry(QtCore.QRect(self.button_x, 210, self.button_width, self.button_height))

        self.pushButton_5.setGeometry(QtCore.QRect(self.button_x, 270, self.button_width, self.button_height))

        self.pushButton_6.setGeometry(QtCore.QRect(self.button_x, 330, self.button_width, self.button_height))

        self.label.setGeometry(QtCore.QRect( self.label_x, self.label_y, self.label_width, self.label_height ))

        self.slider.setGeometry( self.slider_x, self.slider_y, self.slider_width, self.slider_height )

        self.list.setGeometry( self.list_x, self.list_y, self.list_width, self.list_height )

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.pushButton.setText(_translate("TabWidget", "重新播放"))
        self.pushButton_2.setText(_translate("TabWidget", "打开视频"))
        self.pushButton_3.setText(_translate("TabWidget", "保存标签"))
        self.pushButton_4.setText(_translate("TabWidget", "标签路径"))
        self.pushButton_5.setText(_translate("TabWidget", "暂停"))
        self.pushButton_6.setText(_translate("TabWidget", "视频列表"))

        #TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))

        # TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))
        # TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "页"))

