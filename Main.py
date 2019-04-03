from tkinter import *
from tkinter import messagebox
import tkinter as tk
import cv2
import os
import numpy as np
from PIL import Image
import os
from pymongo import MongoClient
from bson.son import SON
from pprint import pprint


client = MongoClient('mongodb://localhost:27017')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadepath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadepath)
db = client.BANK_DATA
global UIN_NO

def face_id():
	cam = cv2.VideoCapture(0)
	cam.set(3,640)
	cam.set(4,480)
	minW = 0.1*cam.get(3)
	minH = 0.1*cam.get(4)
	seconds =0
	while(True):
		ret,img = cam.read()
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor = 1.2,
			minNeighbors = 5,
			minSize = (int(minW) , int(minH)),
			)
		cv2.imshow('camera',img)
		for(x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0), 2)
			id,confidence = recognizer.predict(gray[y:y+h,x:x+w])
			if(confidence < 50):
				count = id
				cam.release()
				cv2.destroyAllWindows()
				return count
			else:
				seconds+=1
				if(seconds==10):
					id = 0
					count = id
					cam.release()
					cv2.destroyAllWindows()
					return count




ARIAL = ("arial",10,"bold")


class Bank:

    UIN_NO = 0
    def __init__(self,root):

        self.login = False
        self.root = root
        self.frame = Frame(self.root,bg="#728B8E",width=800,height=600)

        #Login Page Form Components
        self.userlabel = Label(self.frame,text="WELCOME TO",bg="#728B8E",fg="white",font=("arial",20,"bold"))
        self.plabel = Label(self.frame, text="NEXT GENERATION",bg="#728B8E",fg="white",font=("arial",20,"bold"))
        self.rlabel = Label(self.frame, text="ATM MACHINE",bg="#728B8E",fg="white",font=("arial",20,"bold"))
        self.button = Button(self.frame,text="LOGIN",bg="#50A8B0",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Add Face Id",bg="#50A8B0",fg="white",font=ARIAL,command = self.face)
        self.userlabel.place(x=250,y=60,width=300,height=30)
        self.plabel.place(x=253,y=105,width=300,height=30)
        self.rlabel.place(x=255,y=150,width=300,height=30)
        self.button.place(x=450,y=230,width=140,height=40)
        self.q.place(x=220,y=230,width=140,height=40)
                                                                                                                
        self.frame.pack()

    def face(self):

        self.frame.destroy()
        self.facial_id()



    def facial_id(self):

        self.frame = Frame(self.root,bg="#728B8E",width=1100,height=1100)
        '''This class configures and populates the toplevel window.
        is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.root.geometry("800x450")

        self.Button1 = tk.Button(self.root)
        self.Button1.place(relx=0.391, rely=0.590, height=42, width=208)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''submit''')
        self.Button1.configure(command=self.add_face_recognition)

        self.Entry1 = tk.Entry(self.root)
        self.Entry1.place(relx=0.334, rely=0.373,height=56, relwidth=0.362)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="font13")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.root)
        self.Label1.place(relx=0.034, rely=0.106, height=101, width=787)
        self.Label1.configure(activebackground="#728B8E")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#728B8E")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Black} -size 30 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter Your UIN No''')

        self.frame.pack()


    def add_face_recognition(self):

                cam = cv2.VideoCapture(0)
                cam.set(3, 640)
                cam.set(4, 480) 
                face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


                # For each person, enter one numeric face id
                face_id = int(self.Entry1.get())
                m = "Look the camera and wait ..."
                messagebox._show("message",m)

                # Initialize individual sampling face count
                count = 0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                        count += 1
                        # Save the captured image into the datasets folder
                        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                        cv2.imshow('image', img)
                    k = cv2.waitKey(100) & 0xff 
                    if k == 27:
                        break
                    elif count >= 1000: 
                        break
                                
                cam.release()
                cv2.destroyAllWindows()
                
                        
                # Path for face image database
                path = 'dataset'
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

                # function to get the images and label data
                def getImagesAndLabels(path):
                    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
                    faceSamples=[]
                    ids = []
                    for imagePath in imagePaths:
                        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                        img_numpy = np.array(PIL_img,'uint8')
                        id = int(os.path.split(imagePath)[-1].split(".")[1])
                        faces = detector.detectMultiScale(img_numpy)
                        for (x,y,w,h) in faces:
                            faceSamples.append(img_numpy[y:y+h,x:x+w])
                            ids.append(id)
                    return faceSamples,ids
                m = " It will take a few seconds. Wait ..."
                messagebox._show("message",m)
                faces,ids = getImagesAndLabels(path)
                recognizer.train(faces, np.array(ids))
                # Save the model into trainer/trainer.yml
                recognizer.write('trainer/trainer.yml')
                # Print the numer of faces trained and end program
                m = "Facial Id Added.Thank you!"
                messagebox._show("message",m)
                self.frame.destroy()
                Bank(root)

        

          

        

    def database_fetch(self):#Fetching Account data from database

            self.UIN_NO = face_id()
            if(self.UIN_NO != 0):
                        root.geometry("800x450")
                        name = "Account details"
                        self.frame = Frame(self.root,bg="#728B8E",width=1100,height=1100)
                        self.label = Label(self.frame, bg="#728B8E",text=name, font=("arial",25,"bold"))
                        self.label.place(x=100,y=30,width=600,height=60)
                        details =  "Sl.NO" + "          " +"Account_no" + "              " + "BANK" + "               " + "Account_type" + "          " + "AVAIL_BAL"
                        self.label1 = Label(self.frame, bg="#728B8E", text=details,  font=("arial",15,"bold"))
                        self.label1.place(x=5,y=90,width=800,height=50)
                        for obj in db.DATA_CENTER.find({"UIN" : self.UIN_NO}):

                                count = 1
                                add = 30
                                cookie = []
                                accounts = obj['ACCOUNTS']
                                for i in range(len(accounts)):
                                         if(count!=1):
                                                     details1 = str(count) + "."
                                                     details2 = str(accounts[i]['Account_no'])
                                                     details3 = accounts[i]['BANK']
                                                     details4 = accounts[i]['Account_type'] 
                                                     details5 = str(accounts[i]['AVAIL_BAL'])
                                                     self.label1 = Label(self.frame, bg="#728B8E", text=details1,font=("arial",10,"bold"))
                                                     self.label2 = Label(self.frame, bg="#728B8E", text=details2,font=("arial",10,"bold"))
                                                     self.label3 = Label(self.frame, bg="#728B8E", text=details3,font=("arial",10,"bold"))
                                                     self.label4 = Label(self.frame, bg="#728B8E", text=details4,font=("arial",10,"bold"))
                                                     self.label5 = Label(self.frame, bg="#728B8E", text=details5,font=("arial",10,"bold"))

                                                     self.label1.place(x=30,y=140+add,width=60,height=30)
                                                     self.label2.place(x=130,y=140+add,width=130,height=30)
                                                     self.label3.place(x=300,y=140+add,width=160,height=30)
                                                     self.label4.place(x=485,y=140+add,width=130,height=30)
                                                     self.label5.place(x=633,y=140+add,width=130,height=30)
                                                     add +=30
                                                     count+=1

                                             
                                         if(count==1):
                                                     details1 = str(count) + "."
                                                     details2 = str(accounts[i]['Account_no'])
                                                     details3 = accounts[i]['BANK']
                                                     details4 = accounts[i]['Account_type'] 
                                                     details5 = str(accounts[i]['AVAIL_BAL'])
                                                     self.label1 = Label(self.frame, bg="#728B8E", text=details1,font=("arial",10,"bold"))
                                                     self.label2 = Label(self.frame, bg="#728B8E", text=details2,font=("arial",10,"bold"))
                                                     self.label3 = Label(self.frame, bg="#728B8E", text=details3,font=("arial",10,"bold"))
                                                     self.label4 = Label(self.frame, bg="#728B8E", text=details4,font=("arial",10,"bold"))
                                                     self.label5 = Label(self.frame, bg="#728B8E", text=details5,font=("arial",10,"bold"))

                                                     self.label1.place(x=30,y=140,width=60,height=30)
                                                     self.label2.place(x=130,y=140,width=130,height=30)
                                                     self.label3.place(x=300,y=140,width=160,height=30)
                                                     self.label4.place(x=485,y=140,width=130,height=30)
                                                     self.label5.place(x=633,y=140,width=130,height=30)
                                                     count+=1
                                    
                        self.acc_button = Button(self.frame,bg="#50A8B0", text="Close" ,fg="white", font="arial", command=self.close)
                        self.acc_button.place(x=660, y=370, width=130, height=30)
                        self.frame.pack()
            else:
                    m = "Login Unsuccessful"
                    messagebox._show("Login Info",m)   
       
    

    def verify(self):

            self.UIN_NO = face_id()
            if(self.UIN_NO != 0):
                    m = "Login Successful"
                    messagebox._show("Login Info", m)
                    self.frame.destroy() 
                    self.MainMenu()
            else:
                    m = "Login Unsuccessful"
                    messagebox._show("Login Info",m)
            

            
        
    def MainMenu(self):#Main App Appears after logined !
            
        
        for obj in db.DATA_CENTER.find({"UIN" : self.UIN_NO}):
                name = "WELCOME " + obj['FNAME'] + " " + obj['LNAME']
        self.frame = Frame(self.root,bg="#728B8E",width=1100,height=1100)
        root.geometry("800x450")
        self.label = Label(self.frame, bg="#728B8E",text=name, font=("arial",20,"bold"))
        self.detail = Button(self.frame,text="Account Details",bg="#50A8B0",fg="white",font="arial",command=self.account_detail)
        self.enquiry = Button(self.frame, text="Transfer",bg="#50A8B0",fg="white",font="arial",command= self.transfer)
        self.deposit = Button(self.frame, text="Deposit Money",bg="#50A8B0",fg="white",font="arial",command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money",bg="#50A8B0",fg="white",font="arial",command=self.withdrawl_money)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font="arial", command=self.root.destroy)
        self.label.place(x=150,y=30,width=500,height=60)
        self.detail.place(x=80,y=215,width=200,height=50)
        self.enquiry.place(x=80, y=315, width=200, height=50)
        self.deposit.place(x=525, y=215, width=200, height=50)
        self.withdrawl.place(x=525, y=315, width=200, height=50)
        self.q.place(x=335, y=380, width=140, height=30)
        self.frame.pack()

    def account_detail(self):

        self.frame.destroy() 
        self.database_fetch()

    def transfer(self):

        self.frame.destroy()
        self.transfer_money()

    def close(self):

        self.frame.destroy()
        Bank(root)

    def back_mainmenu(self):

        self.frame.destroy()
        self.MainMenu()

    def deposit_money(self):
        
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)

        self.money_box.place(x=290,y=150,width=200,height=30)
        self.submitButton.place(x=500,y=150,width=55,height=30)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):

        for obj in db.DATA_CENTER.find({"UIN" : self.UIN_NO}):
                i=0
                accounts = obj['ACCOUNTS']
                amount = accounts[i]['AVAIL_BAL'] + int(self.money_box.get())
                db.DATA_CENTER.update({'UIN' : self.UIN_NO, "ACCOUNTS.Account_no" : accounts[i]['Account_no']},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate":{"lastModified":True}})
        self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
        self.label.place(x=250, y=100, width=300, height=100)
        m = "Transaction Completed !"
        messagebox._show("Transaction Info", m)
        self.frame.destroy()
        Bank(root)
        

    def withdrawl_money(self):
        
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)
        self.money_box.place(x=290,y=150,width=200,height=30)
        self.submitButton.place(x=500,y=150,width=55,height=30)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self,flag):

        for obj in db.DATA_CENTER.find({"UIN" : self.UIN_NO}):
                i=0
                accounts = obj['ACCOUNTS']
                if(accounts[i]['AVAIL_BAL'] >= int(self.money_box.get())):
                        amount = accounts[i]['AVAIL_BAL'] - int(self.money_box.get())
                        db.DATA_CENTER.update({'UIN' : self.UIN_NO, "ACCOUNTS.Account_no" : accounts[i]['Account_no']},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate":{"lastModified":True}})
                        self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
                        self.label.place(x=250, y=100, width=300, height=100)
                        m = "Transaction Completed !"
                        messagebox._show("Transaction Info", m)
                        self.frame.destroy()
                        Bank(root)
                else:

                        m = "Insufficient Balance !"
                        messagebox._show("Transaction Info", m)
                        self.frame.destroy()
                        Bank(root)


    def proceed(self):
            
        for obj in db.DATA_CENTER.find({"UIN" : self.UIN_NO}):
                i=0
                accounts = obj['ACCOUNTS']
                if(accounts[i]['AVAIL_BAL'] >= int(self.Entry4.get())):
                        amount = accounts[i]['AVAIL_BAL'] - int(self.Entry4.get())
                        db.DATA_CENTER.update({'UIN' : self.UIN_NO, "ACCOUNTS.Account_no" : accounts[i]['Account_no']},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate":{"lastModified":True}})
                        for obj in db.DATA_CENTER.find({"UIN" : int(self.Entry0.get())}):
                                        accounts = obj['ACCOUNTS']
                                        for i in range(len(accounts)):
                                                        if(accounts[i]['Account_no'] == int(self.Entry1.get())):
                                                                amount = accounts[i]['AVAIL_BAL'] + int(self.Entry4.get())
                                        db.DATA_CENTER.update({'UIN' : int(self.Entry0.get()),"ACCOUNTS.Account_no" : int(self.Entry1.get())},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate": {"lastModified": True}})        
                else:

                        m = "Insufficient Balance !"
                        messagebox._show("Transaction Info", m)
                        self.frame.destroy()
                        Bank(root)
    
       
        
                m = "Transfer Complete"
                messagebox._show("Transfer Info", m)
                self.frame.destroy()
                Bank(root)
        
        

    def transfer_money(self):
            
        '''This class configures and populates the toplevel window.
         top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'
        font10 = "-family {Segoe UI Black} -size 16 -weight bold"
        font12 = "-family {Segoe UI Black} -size 23 -weight bold"
        font13 = "-family {@Malgun Gothic} -size 13 -weight bold"

        root.geometry("800x450")
        root.configure(background="#d9d9d9")

        self.frame = Frame(self.root,bg="#728B8E",width=1100,height=1100)
        
        self.Button1 = tk.Button(self.frame)
        self.Button1.place(relx=0.598, rely=0.835, height=50, width=208)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Proceed''')
        self.Button1.configure(width=208)
        self.Button1.configure(command=self.proceed)

        self.Button2 = tk.Button(self.frame)
        self.Button2.place(relx=0.157, rely=0.835, height=50, width=208)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font13)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Cancel''')
        self.Button2.configure(width=208)
        self.Button2.configure(command=self.back_mainmenu)

        self.Label0 = tk.Label(self.frame)
        self.Label0.place(relx=0.1, rely=0.210, height=51, width=302)
        self.Label0.configure(background="#728B8E")
        self.Label0.configure(disabledforeground="#a3a3a3")
        self.Label0.configure(font=font10)
        self.Label0.configure(foreground="#000000")
        self.Label0.configure(text='''Unique Identifcation Number''')
        self.Label0.configure(width=247)

        self.Entry0 = tk.Entry(self.frame)
        self.Entry0.place(relx=0.588, rely=0.223,height=36, relwidth=0.269)
        self.Entry0.configure(background="white")
        self.Entry0.configure(disabledforeground="#a3a3a3")
        self.Entry0.configure(font="TkFixedFont")
        self.Entry0.configure(foreground="#000000")
        self.Entry0.configure(insertbackground="black")
        self.Entry0.configure(width=324)

        self.Entry1 = tk.Entry(self.frame)
        self.Entry1.place(relx=0.588, rely=0.343,height=36, relwidth=0.269)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=324)

        self.Label1 = tk.Label(self.frame)
        self.Label1.place(relx=0.035, rely=0.320, height=51, width=287)
        self.Label1.configure(background="#728B8E")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Account Number''')
        self.Label1.configure(width=287)

        self.Label2 = tk.Label(self.frame)
        self.Label2.place(relx=0.0008, rely=0.436, height=51, width=407)
        self.Label2.configure(background="#728B8E")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Account Holder's Name''')
        self.Label2.configure(width=407)

        self.Entry2 = tk.Entry(self.frame)
        self.Entry2.place(relx=0.588, rely=0.461,height=36, relwidth=0.269)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=324)

        self.Label3 = tk.Label(self.frame)
        self.Label3.place(relx=0.010, rely=0.05, height=70, width=757)
        self.Label3.configure(background="#728B8E")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter Account Details''')
        self.Label3.configure(width=757)

        self.Label4 = tk.Label(self.frame)
        self.Label4.place(relx=0.004, rely=0.565, height=51, width=267)
        self.Label4.configure(background="#728B8E")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''IFSC Code''')
        self.Label4.configure(width=267)

        self.Entry3 = tk.Entry(self.frame)
        self.Entry3.place(relx=0.588, rely=0.580,height=36, relwidth=0.269)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=324)

        self.Label5 = tk.Label(self.frame)
        self.Label5.place(relx=0.008, rely=0.686, height=51, width=247)
        self.Label5.configure(background="#728B8E")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Amount''')
        self.Label5.configure(width=247)

        self.Entry4 = tk.Entry(self.frame)
        self.Entry4.place(relx=0.588, rely=0.698,height=36, relwidth=0.269)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=324)

        self.frame.pack()



root = Tk()

root.title("ATM PROJECT")
root.geometry("800x450")
icon = PhotoImage(file="icon.png")
root.tk.call("wm",'iconphoto',root._w,icon)
header = Label(root,text="ATM PROJECT",bg="#50A8B0",fg="white",font=("arial",20,"bold"))
header.pack(fill=X)
obj = Bank(root)
root.mainloop()

'''If you like this project give a star ,,,,,,Thanks !'''
