# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:31:38 2020

@author: Valay
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:02:50 2020

@author: Valay
"""

import cv2
import os
import face_recognition
#from pymongo import MongoClient
#from random import randint
import csv
import webbrowser
from django.shortcuts import render
#import requests

#Face Detection Code
def button(request):
    return render(request,'home.html')
def output(request):
    face_cascade = cv2.CascadeClassifier("/media/valay/E Drive/sem8/project/haarcascades/haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    a = 1

    face_cascade = cv2.CascadeClassifier('/media/valay/E Drive/sem8/project/haarcascades/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
 
    while True:
        a = a + 1
        _, img = video.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=5)
  
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 3)
      
            #eye_gray = gray[y:y+h, x:x+w]
            #eye_color = img[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(eye_gray)
    
   
        cv2.imshow("capture",img)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        if key & 0xFF == ord('c'):
            crop_img = img[y: y + h, x: x + w] 
            cv2.imwrite("my_image.jpg", crop_img)

    print(a) #This will print the number of frames
    video.release()
    cv2.destroyAllWindows()



    images = os.listdir('/media/valay/E Drive/sem8/project/images')


    image_to_be_matched = face_recognition.load_image_file('my_image.jpg')


    image_to_be_matched_encodeded = face_recognition.face_encodings(image_to_be_matched)
    print("hello",type(image_to_be_matched_encodeded))
    image_to_be_matched_encoded = []
    if len(image_to_be_matched_encodeded)>0:
        image_to_be_matched_encoded = image_to_be_matched_encodeded[0]

    
    for image in images:
    
        current_image = face_recognition.load_image_file("/media/valay/E Drive/sem8/project/images/" + image)
    
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
    
        result = face_recognition.compare_faces(
                [image_to_be_matched_encoded], current_image_encoded)
    
        if result[0] == True:
            print ("Matched: " + image)
        
            a=''
            b=0
            c=''
            result1 = ""
            result1 = result1.join(image)
            print(result1)
            img = result1.split(".")
            print(img[0])
            with open('/media/valay/E Drive/sem8/project/data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[3]==img[0]:
                        a=row[0]
                        b=row[1]
                        c=row[2]
            print(a,b,c)
            f = open('helloworld12.html','w')
            x="valay"
            y="shah"
            message = """<html>
            <head></head>
            <body style="background-color:grey;">
            <h2 style="text-align:center">SEM 8 Project Form</h2>

            <form action="/action_page.php">
            <label for="fname">First name:</label><br>
            <input type="text" id="fname" name="fname" value="%s"><br>
            <label for="lname">age:</label><br>
            <input type="text" id="age" name="age" value="%s"><br><br>
            <label for="lname">gender:</label><br>
            <input type="text" id="gender" name="gender" value="%s"><br><br>
            <input type="submit" value="Submit">
            </form> 

            
            </body>
            </html>"""

#new_message = message.format(y=x)
            whole=message %(a,b,c)
            f.write(whole)
            f.close()

            webbrowser.open_new_tab('/media/valay/E Drive/sem8/project/sem8_django/helloworld12.html')
        else:
            print("not matched"+image)
    return render(request,'home.html',{'data':image})
    
                    
        #client = MongoClient('mongodb+srv://dhruv_98:Microsoft68@cluster0-uccqv.mongodb.net/test?retryWrites=true&w=majority')
        #db=client.medical
        #for doc in db.medical.find():
          #print("Hello")
    
    
   
        #else:
            #print ("Not matched: " + image)
    #return render(request,'home.html',{'data':image})
        #client = MongoClient('mongodb+srv://dhruv_98:Microsoft68@cluster0-uccqv.mongodb.net/test?retryWrites=true&w=majority')
        #db=client.medical
        #for doc in db.medical.find():
          #print("Hello")
    
    
   
    
