import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QImage
import numpy as np
import cv2
import sys
import os
import PyQt5 as Qt
from elements.yolo import OBJ_DETECTION 
import pathlib
import pyttsx3 as tx
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


class MainWindow(QDialog):
    global frame
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("front.ui",self)
        self.cbt1.clicked.connect(self.goto_cam)
        self.bbt2.clicked.connect(self.goto_Browse)
        #self.stop.clicked.connect(self.save)
        
    def goto_cam(self):
        S = Camera()
        widget.addWidget(S)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    
    def goto_Browse(self):
        S = Browsefiles()
        widget.addWidget(S)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Browsefiles(QDialog):
    def __init__(self):
        super(Browsefiles,self).__init__()
        loadUi("screenq.ui",self)        
        self.bt1.clicked.connect(self.browse)
        self.bt2.clicked.connect(self.test)
        self.bt2_2.clicked.connect(self.gotoBack)
        
        
        
    def browse(self):
        
        global fname
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Images (*.png *.xmp *.jpeg *.jpg)')
        #self.imageview.setPixmap(QtGui.QPixmap(fname))
        pixmap = QtGui.QPixmap(fname)
        pixma4 = pixmap.scaled(500,500)
        self.imageview.setPixmap(pixma4)
        
    def test(self):
        
        Object_classes = ['mouse_bite','spur','missing_hole','short','open_circuit','spurious_copper','scratch']

        Object_colors = list(np.random.rand(40,3)*255) 
        Object_detector = OBJ_DETECTION('best1.pt', Object_classes) 
        
        cap = cv2.imread(fname)
        
                            
        objs = Object_detector.detect(cap) 
        
        flag =0
        
        while True:
            if len(objs) >1:
                flag=1
            
            def audio():
                engine = tx.init()
                engine.say("more defects detected ")
                engine.runAndWait() 
                
                
            for obj in objs:
                
            
                    label = obj['label'] 
            
                    score = obj['score'] 
             
                    if label == 'mouse_bite':
                            print(score)
                            print('mouse_bite')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Mouse bite')
                            if flag == 1:
                                audio()
                            
                    elif label == 'spur':
                            print(score)
                            print('spur')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Spur')
                            if flag == 1:
                                audio()
                            
                    elif label == 'missing_hole':
                            print(score)
                            print('missing_hole')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Missing hole')
                            if flag == 1:
                                audio()
                            
                    elif label == 'short':
                            print(score)
                            print('short')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Short')
                            if flag == 1:
                                audio()
                            
                    elif label == 'open_circuit':
                            print(score)
                            print('open_circuit')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Open circuit')
                            if flag == 1:
                                audio()
                            
                    elif label == 'spurious_copper':
                            print(score)
                            print('spurious_copper')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('Spurious copper')
                            if flag == 1:
                                audio()
                            
                    elif label == 'scratch':
                            print(score)
                            print('scratch')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('scratch')
                            if flag == 1:
                                audio()
                    else:
                        pass
                    
            cv2.imshow('frame',cap)                
            #
            keyCode = cv2.waitKey(0) 
            if keyCode == ord('q'): 
                break 
        cv2.destroyAllWindows() 


        
        
        
    def gotoBack(QDialog):
         mainwindow = MainWindow()
         widget.addWidget(mainwindow)
         widget.setCurrentIndex(widget.currentIndex()+1)  
         
        
class Camera(QDialog):
    def __init__(self):
        super(Camera,self).__init__()
        loadUi("camera.ui",self)        
        self.load_btn.clicked.connect(self.video)
        self.CPbt2.clicked.connect(self.test)
        self.CBbt1.clicked.connect(self.gotoBack)      
    def video(self):
        
 
        cap = cv2.VideoCapture(0)
        
        while True:
            
            _,frame = cap.read()
            

            cv2.imshow("window",frame)
            
            q=cv2.waitKey(1)
            
            if q == ord('q'):
                cv2.imwrite('first.jpg',frame)
                break
  
        cap.release()
        cv2.destroyAllWindows()
        self.imageview_camera.setPixmap(QtGui.QPixmap('first.jpg'))

       
    def test(self):
        
        Object_classes = ['mouse_bite','spur','missing_hole','short','open_circuit','spurious_copper','scratch']

        Object_colors = list(np.random.rand(40,3)*255) 
        Object_detector = OBJ_DETECTION('best1.pt', Object_classes) 
        
        cap = cv2.imread('first.jpg')
        
                            
        objs = Object_detector.detect(cap) 
        
        flag =0
        
        while True:
        
            for obj in objs:
            
                    label = obj['label'] 
            
                    score = obj['score'] 
             
                    if label == 'mouse_bite':
                            print(score)
                            print('mouse_bite')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('mouse_bite')
                            
                            
                    elif label == 'spur':
                            print(score)
                            print('spur')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('spur')
                            
                            
                    elif label == 'missing_hole':
                            print(score)
                            print('missing_hole')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('missing_hole')
                            
                            
                    elif label == 'short':
                            print(score)
                            print('short')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('short')
                            
                            
                    elif label == 'open_circuit':
                            print(score)
                            print('open_circuit')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('open_circuit')
                            
                            
                    elif label == 'spurious_copper':
                            print(score)
                            print('spurious_copper')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('spurious_copper')
                            
                            
                    elif label == 'scratch':
                            print(score)
                            print('scratch')
                            [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                            color = Object_colors[Object_classes.index(label)] 
                            frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                            self.label_2.setText('scratch')
                            
                    else:
                        pass
                    
            cv2.imshow('frame',cap)                
            #
            keyCode = cv2.waitKey(0) 
            if keyCode == ord('q'): 
                break 
        cv2.destroyAllWindows() 
            
    def gotoBack(QDialog):
         mainwindow = MainWindow()
         widget.addWidget(mainwindow)
         widget.setCurrentIndex(widget.currentIndex()+1)      
      
app=QApplication(sys.argv)
mainwindow = MainWindow()
widget=QtWidgets.QStackedWidget()

widget.addWidget(mainwindow)
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())