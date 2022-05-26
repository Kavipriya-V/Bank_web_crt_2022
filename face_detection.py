import cv2, sys, numpy, os
from face_liveness_detection_Anti_spoofing_master.face_anti_spoofing import liveness
def get(username):
    webcam = cv2.VideoCapture(0) 

    val = liveness(webcam)
    if val == 'fail':
        print('your not allowed to register')
        webcam.release()
        cv2.destroyAllWindows()
        return 'your not allowed to register'
    else:
        haar_file = "haarcascade_frontalface_alt2.xml"
        datasets = './datasets'  
        sub_data= username
        path = os.path.join(datasets, sub_data) 
        if not os.path.isdir(path):
            os.mkdir(path)   
        (width, height) = (130, 100)   
        face_cascade=cv2.CascadeClassifier(haar_file)  
         
        count = 1
        while count<70:  
            (_, im) = webcam.read() 
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
            faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
            for (x, y, w, h) in faces: 
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                face = gray[y:y + h, x:x + w] 
                face_resize = cv2.resize(face, (width, height)) 
                cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
            count += 1
            cv2.imshow('OpenCV', im) 
            key = cv2.waitKey(10) 
            if key == 27: 
                break
            
        webcam.release()
        cv2.destroyAllWindows()