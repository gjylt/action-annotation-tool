import sys, cv2, time
from x import Ui_TabWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QTabWidget
from PyQt5.QtCore import    QTimer, QThread, pyqtSignal, Qt
from PyQt5.QtGui import     QPixmap, QImage
from PyQt5.QtWidgets import QLabel,QWidget
import os
import tkinter as tk
from tkinter import filedialog
import json

#这个窗口继承了用 QtDesignner 绘制的窗口
class mywindow(QTabWidget,Ui_TabWidget):

    #changeSliderv = pyqtSignal(float)

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

        self.slider.setMinimum(0)

        self.th = Thread( self)
        self.th.changePixmap.connect(self.setImage)
        self.th.changeframeC.connect(self.ChangeSliderValue)
        self.th.changeslideMax.connect(self.ChangeSliderMax)

        #self.slider.valueChanged.connect(self.SliderValueChanged)
        self.slider.sliderMoved.connect(self.SliderValueChanged)

        self.current_play_videoname = ""
        self.annotation_dri = './'

    def paintEvent(self, evt):
        #print("paint")
        #print(self.size())
        tmp = 0

    def resizeEvent(self, QResizeEvent):


        w = self.size().width()
        h = self.size().height()


        #self.label.resize( QtCore.QSize( int(w*self.label_width), int(h*self.label_hight)))

        label_h = int(h*self.label_h_ration)
        label_w = int(w*self.label_w_ration)
        self.label.setGeometry(QtCore.QRect(110, 30,  label_w, label_h ))

        self.slider.setGeometry(110, label_h+30+30, label_w, 30)

        l_h = self.label.size().width()
        l_w = self.label.size().height()

        l_h = l_h * 1.0 / h
        l_w = l_w*1.0/w

        print(l_h,self.label_h_ration,l_w,self.label_w_ration )


        print("resize")



    def ChangeSliderMax(self,max):
        self.slider.setMaximum(max)
        self.frameMax = max

    def SliderValueChanged( self, value ):

        self.slidervalue = value
        self.th.changeframe(value)
        time.sleep(1.0/30)
        self.th.move_slider = True
        #print("SliderValueChanged", value)


    def ChangeSliderValue( self, value ):

        #if (self.slider.sliderPressed() == False):

        self.slider.setValue(int(value))


        #print("ChangeSliderValue",value)



    def videoprocessing(self):

        print("gogo")

        if self.current_play_videoname != "":
            self.saverannotation()

        videoName,videoType= QFileDialog.getOpenFileName(self,
                                                        "打开视频",
                                                         "./avi",
                                                            "*.avi;;*.mp4;;All Files (*)"
                                                         )

        if videoName != "":
            self.current_play_videoname = videoName
            self.th.setVideoName(videoName)

            self.th.start()


    def setImage(self, image):
        #sz = self.label.shape
        self.label.setPixmap(QPixmap.fromImage(image))



    def ReplayVideo(self):
        self.th.StopPlay = True
        self.th.setVideoName( self.current_play_videoname )
        time.sleep(0.1)  # 控制视频播放的速度
        self.th.StopPlay = False
        self.th.start()

    def keyPressEvent(self, event):

        # 这里event.key（）显示的是按键的编码
        #print("按下：" + str(event.key())) # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_S):
            self.th.Press_KeyS()
            print('开始做标签')
        if (event.key() == Qt.Key_E):
            self.th.Press_KeyE()
            print('结束做标签')
        if (event.key() == Qt.Key_D):
            self.th.delList()
            print('删除标签')

        if (event.key() == Qt.Key_I):
            self.th.change_frame_step( True)
            print('增加')
        if (event.key() == Qt.Key_K):
            self.th.change_frame_step(False)
            print('减少')
        if (event.key() == Qt.Key_L):
            self.th.step_change_frame( True)
            print('前进')
        if (event.key() == Qt.Key_J):
            self.th.step_change_frame( False)
            print('后退')

        if (event.key() == Qt.Key_Enter):
            print('测试：Enter')
        if (event.key() == Qt.Key_Space):
            print('测试：Space')

    def saverannotation(self):
        self.th.StopPlay = True

        name = self.current_play_videoname.split('/')[-1].split('.')[0]
        pth = self.annotation_dri + name + '.json'
        self.th.save_json(pth)
        time.sleep(0.1)
        self.th.StopPlay = False

    def setsavepath(self):

        file_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")

        self.annotation_dri = file_path
        #print(self.annotation_dri)




#采用线程来播放视频
class Thread(QThread):
    changePixmap = pyqtSignal(QtGui.QImage) #刷新界面显示的图像
    changeframeC = pyqtSignal(int)          #给slider发送当前的帧索引
    changeslideMax = pyqtSignal(int)        #修改slider的最大滑动范围

    create_new_annotation = False
    rangelist = []
    StopPlay  = False
    new_annotation_index = 0
    annotation_dri = './'
    video_play_pause = False
    frame_step = 1
    move_slider = False


    def load_json(self,pth):

        fr = open(pth)
        model = json.load(fr)
        fr.close()

        return model



    def save_json(self,pth):

        if len(self.rangelist) > 0:
            jsObj = json.dumps(self.rangelist)
            with open(pth, "w") as fw:
                fw.write(jsObj)
            fw.close()

        #
    def run(self):
        cap             = cv2.VideoCapture(self.videoname)
        self.framenum   = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        framerate       = 30 #int(cap.get(cv2.CAP_PROP_FPS))
        cap.set(cv2.CAP_PROP_FPS, framerate)


        self.changeslideMax.emit( self.framenum )
        self.frame_c = 0

        name = self.videoname.split('/')[-1].split('.')[0]

        pth = self.annotation_dri + name + '.json'
        if os.path.exists(pth) and os.path.isfile(pth):
            self.rangelist =  self.load_json(pth)

        while (cap.isOpened() ==True  ):

            if self.StopPlay:
                break

            #暂停
            while(self.video_play_pause):
                tmp = 1

            #print(self.frame_c)

            if self.move_slider:
                cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_c )
                self.move_slider = False

            #videoframe = cap.get(cv2.CAP_PROP_POS_FRAMES)

            #print("current video frame",videoframe,self.frame_c )

            ret, frame   = cap.read()

            if ret:

                value = self.frame_c*1.0/self.framenum


                self.flush_E(value)

                shp = frame.shape #h,w,c
                tmp1 =  [ i for i in range(0, 0)]
                for rang in self.rangelist:
                    tmp = [i for i in range( int(shp[1]*rang[0]), int(shp[1]*rang[1]))]
                    tmp1 = tmp + tmp1
                frame[int(0.9*shp[0]):shp[0],tmp1,1] = 255


                cv2.putText(frame, 'step:'+str(self.frame_step), (20, 20), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 0, 0), 2, 1)

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)#在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(461, 311, Qt.KeepAspectRatio)

                #发送图片 刷新显示
                self.changePixmap.emit(p)


            time.sleep(1.0/framerate) #控制视频播放的速度

            self.frame_c = self.frame_c + 1
            # 改变 slider 进度
            self.changeframeC.emit(self.frame_c)

        cap.release()

        name = self.videoname.split('/')[-1].split('.')[0]
        pth = self.annotation_dri + name + '.json'
        self.save_json(pth)


    def changeframe(self,value):
        self.frame_c = value
        #print("th changeframe",self.frame_c)

    def step_change_frame(self,isForward):
        if isForward:
            tmp     = self.frame_c + self.frame_step
            if tmp > self.framenum:
                tmp = self.framenum-1
            if tmp < 0:
                tmp = 0
            self.frame_c = tmp
        else:
            tmp     = self.frame_c - self.frame_step
            if tmp > self.framenum:
                tmp = self.framenum-1
            if tmp < 0:
                tmp = 0
            self.frame_c = tmp
        self.move_slider = True
        time.sleep(1.0/30)

    def change_frame_step(self,isAdd):
        if isAdd:
            self.frame_step = self.frame_step +1
        else:
            self.frame_step = self.frame_step -1

    def setVideoName(self,name):
        self.videoname = name

    def Press_KeyS(self):

        self.video_play_pause = True

        value = self.frame_c*1.0/self.framenum

        if value < 0 or value > 1:
            self.video_play_pause = False
            return

        for idx,range in enumerate(self.rangelist):

            if value >= range[0] and value <= range[1]:
                self.rangelist[idx][0] = value
                self.video_play_pause  = False
                return

        tmp = [value,value]
        self.rangelist.append(tmp)
        self.create_new_annotation = True
        self.new_annotation_index = len(self.rangelist)-1
        self.video_play_pause = False


    def Press_KeyE(self):

        self.video_play_pause = True
        value = self.frame_c*1.0/self.framenum

        if value < 0 or value > 1:
            self.video_play_pause = False
            return

        if self.create_new_annotation :

            self.rangelist[self.new_annotation_index][1] = value
            #合并重叠的标签

            #退出创建新标签状态
            self.create_new_annotation = False
            self.video_play_pause = False
            return
        else:
            for idx,range in enumerate(self.rangelist):
                if value >= range[0] and value <= range[1]:
                    self.rangelist[idx][1] = value
                    self.video_play_pause = False
                    return
            self.video_play_pause = False

    def flush_E(self,value):
        if self.create_new_annotation:
            self.rangelist[self.new_annotation_index][1] = value

    def delList(self):

        if self.create_new_annotation == False:

            value = self.frame_c * 1.0 / self.framenum
            lis_idx = -1
            for idx, range in enumerate(self.rangelist):
                if value >= range[0] and value <= range[1]:
                    lis_idx = idx
                    break

            if lis_idx >= 0 and lis_idx < len(self.rangelist):
                del self.rangelist[lis_idx]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())

