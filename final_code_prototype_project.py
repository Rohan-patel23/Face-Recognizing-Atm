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
			if(confidence < 50 ):
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
				
	
print("////////////////////////////////////////////")
print("//                                        //")
print("//                                        //")
print("//               WELCOME                  //")
print("//                 TO                     //")
print("//            DIGITAL INDIA               //")
print("//                                        //")
print("//                                        //")
print("////////////////////////////////////////////")


flag = 1


while(flag!=0):

	print(" ")
	print("WHAT WOULD YOU LIKE TO DO")
	print(" ")
	print("PRESS 1 TO WITHDRAWL ")
	print("PRESS 2 TO DEPOSIT ")
	print("PRESS 3 TO CHECK BALANCE ")
	print("PRESS 0 TO ADD YOUR FACE ID TO YOUR ACCOUNT")
	print(" ")
	choice = int(input("ENTER YOUR CHOICE :"))


    # Withdrawl of money
	if(choice == 1):
		# Identifying the face 
		print("Show your face for face id")
		UIN_NO = face_id()
		#Data Transaction
		if(UIN_NO != 0):
			for obj in db.DATA_CENTER.find({"UIN" : UIN_NO}):
				print( "WELCOME " + obj['FNAME'] + " " + obj['LNAME'])
				accounts = obj['ACCOUNTS']
				print("Press 1 for SAVINGS ACCOUNT or PRESS 2 for CURRENT ACCOUNT ")
				acc_type = int(input())
				count = 1
				cookie = []
				for i in range(len(accounts)):
					if(acc_type == 1 and accounts[i]['Account_type'] == "SAVINGS"):
						print(str(count) + ")"+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'])
						cookie.append(accounts[i]['Account_no'])
						count+=1
					if(acc_type == 2 and accounts[i]['Account_type'] == "CURRENT"):
						print(str(count) + ")"+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'])
						cookie.append(accounts[i]['Account_no'])
						count+=1
				choose = int(input("Choose The Account :"))
				amount = int(input("Enter the amount :"))
				for i in range(len(accounts)):
					if(accounts[i]['Account_no'] == cookie[choose-1] and amount <= accounts[i]['AVAIL_BAL']):
						amount = accounts[i]['AVAIL_BAL'] - amount
				db.DATA_CENTER.update({'UIN' : UIN_NO,"ACCOUNTS.Account_no" : cookie[choose-1]},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate": {"lastModified": True}})
			close = input("WOULD YOU LIKE TO DO ANOTHER TRANSACTION 'Y'/'N' : ")
			if(close.upper()=='Y'):
				flag=1
			elif(close.upper()=='N'):
				flag=0
		elif(UIN_NO==0):
			print("INVALID FACIAL ID")
			flag=0
				   
	

    # Money Deposit
	if(choice == 2):
		#Identifying the face
		print("Show your face for face id")
		UIN_NO = face_id()
		#Data Transaction
		if(UIN_NO != 0):
			for obj in db.DATA_CENTER.find({"UIN" : UIN_NO}):
				print( "WELCOME " + obj['FNAME'] + " " + obj['LNAME'])
				accounts = obj['ACCOUNTS']
				print("Press 1 for SAVINGS ACCOUNT or PRESS 2 for CURRENT ACCOUNT ")
				acc_type = int(input())
				count = 1
				cookie = []
				for i in range(len(accounts)):
					if(acc_type == 1 and accounts[i]['Account_type'] == "SAVINGS"):
						print(str(count) + ")"+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'])
						cookie.append(accounts[i]['Account_no'])
						count+=1
					if(acc_type == 2 and accounts[i]['Account_type'] == "CURRENT"):
						print(str(count) + ")"+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'])
						cookie.append(accounts[i]['Account_no'])
						count+=1
				choose = int(input("Choose The Account :"))
				amount = int(input("Enter the amount :"))
				for i in range(len(accounts)):
					if(accounts[i]['Account_no'] == cookie[choose-1]):
						amount = accounts[i]['AVAIL_BAL'] + amount
				db.DATA_CENTER.update({'UIN' : UIN_NO,"ACCOUNTS.Account_no" : cookie[choose-1]},{"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},"$currentDate": {"lastModified": True}})
			close = input("WOULD YOU LIKE TO DO ANOTHER TRANSACTION 'Y'/'N' : ")
			if(close.upper()=='Y'):
				flag=1
			elif(close.upper()=='N'):
				flag=0
		elif(UIN_NO==0):
			print("INVALID FACIAL ID")
			flag=0





		

               
		
		
    # To check Account Balance
	if(choice == 3):
		print("Show your face for face id")
		UIN_NO = face_id()
		#Tracsaction of data
		if(UIN_NO != 0):
			for obj in db.DATA_CENTER.find({"UIN" : UIN_NO}):
				print( "WELCOME " + obj['FNAME'] + " " + obj['LNAME'])
				accounts = obj['ACCOUNTS']
				print("Press 1 for SAVINGS ACCOUNT or PRESS 2 for CURRENT ACCOUNT ")
				acc_type = int(input())
				count = 1
				cookie = []
				for i in range(len(accounts)):
					if(acc_type == 1 and accounts[i]['Account_type'] == "SAVINGS"):
						print(str(count) + ")."+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'] + " " + str(accounts[i]['AVAIL_BAL']))
						cookie.append(accounts[i]['Account_no'])
						count+=1
					if(acc_type == 2 and accounts[i]['Account_type'] == "CURRENT"):
						print(str(count) + ")."+ str(accounts[i]['Account_no']) + " " + accounts[i]['BANK'] + " " + str(accounts[i]['AVAIL_BAL']))
						cookie.append(accounts[i]['Account_no'])
						count+=1
			close = input("WOULD YOU LIKE TO DO ANOTHER TRANSACTION 'Y'/'N' : ")
			if(close.upper()=='Y'):
				flag=1
			elif(close.upper()=='N'):
				flag=0
		elif(UIN_NO==0):
			print("INVALID FACIAL ID")
			flag=0





   #To add facial id to your account 
	if(choice == 0):
		cam = cv2.VideoCapture(0)
		cam.set(3, 640) # set video width
		cam.set(4, 480) # set video height
		face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


		# For each person, enter one numeric face id
		face_id = input('\n enter UIN Number end press <return> ==>  ')
		print("\n [INFO] Initializing face capture. Look the camera and wait ...")


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
		    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		    if k == 27:
		        break
		    elif count >= 1000: # Take 30 face sample and stop video
		        break
		        
		# Do a bit of cleanup
		print("\n [INFO] Exiting Program and cleanup stuff")
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
		print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
		faces,ids = getImagesAndLabels(path)
		print(ids)
		recognizer.train(faces, np.array(ids))

		# Save the model into trainer/trainer.yml
		recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
		# Print the numer of faces trained and end program
		print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


print("THANK YOU FOR USING OUR ATM")
    

   	
    
