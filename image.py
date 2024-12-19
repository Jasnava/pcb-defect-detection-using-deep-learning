import cv2 
import numpy as np 
from elements.yolo import OBJ_DETECTION 
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

Object_classes = ['mouse_bite','spur','missing_hole','short','open_circuit','spurious_copper','scratch']

Object_colors = list(np.random.rand(40,3)*255) 
Object_detector = OBJ_DETECTION('best1.pt', Object_classes)

cap = cv2.imread('mh2.jpg')
#cap = cv2.resize(cap,(512,512))               
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
                                    
            elif label == 'spur':
                    print(score)
                    print('spur')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                                    
            elif label == 'missing_hole':
                    print(score)
                    print('missing_hole')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                                    
            elif label == 'short':
                    print(score)
                    print('short')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                                    
            elif label == 'open_circuit':
                    print(score)
                    print('open_circuit')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                                    
            elif label == 'spurious_copper':
                    print(score)
                    print('spurious_copper')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 
                                    
            elif label == 'scratch':
                    print(score)
                    print('scratch')
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    color = Object_colors[Object_classes.index(label)] 
                    frame = cv2.rectangle(cap, (xmin+50,ymin+50), (xmax-50,ymax-50), color, 2) 
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+50,ymin+50),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA) 

            else:
                pass
                      
    cv2.imshow("window", cap) 
    keyCode = cv2.waitKey(0) 
    if keyCode == ord('q'): 
        break 
cv2.destroyAllWindows() 


       

