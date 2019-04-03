# Import the python libraries
from pymongo import MongoClient
from bson.son import SON
from pprint import pprint
# Choose the appropriate client
client = MongoClient('mongodb://localhost:27017')

db = client.BANK_DATA

##db.DATA_CENTER.insert_many([
##
##    {   "UIN" : 316874311,
## 	    "FNAME" : "ROHAN",
## 	    "LNAME" : "PATEL",
## 	    "FULL_ADDRESS" : "NEAR JP EVENING COLLEGE,HILL TOWN,BHAWANIPATNA,KALAHANDHI,ODISHA", 
## 	    "CITY/TOWN" : "BHAWANIPATNA",
## 	    "STATE" : "ODISHA",
## 	    "PINCODE" : 766001,
## 	    "PHONE_NUMBER" : 8249847076,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 7894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7894651238), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874312,
## 	    "FNAME" : "LOKENDRA",
## 	    "LNAME" : "SINGH",
## 	    "FULL_ADDRESS" : "DILBAGH NAGAR,BHWANI MANDI,KOTA,RAJASTHAN,", 
## 	    "CITY/TOWN" : "BHWANI MANDI",
## 	    "STATE" : "RAJASTHAN",
## 	    "PINCODE" : 326502,
## 	    "PHONE_NUMBER" : 8455026676,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 9894651234), ("BANK", "ORIENTAL BANK OF COMMERCE"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 9894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 9894651238), ("BANK", "BANK OF BARODA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 9894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874313,
## 	    "FNAME" : "SHUVANKAN ARKALOK",
## 	    "LNAME" : "DAS",
## 	    "FULL_ADDRESS" : "NEAR MISTI BAAZAR,KOLKATA,WEST BENGAL", 
## 	    "CITY/TOWN" : "KOLKATA",
## 	    "STATE" : "WEST BENGAL",
## 	    "PINCODE" : 700002,
## 	    "PHONE_NUMBER" : 7249547076,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 6894651234), ("BANK", "DENA BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 6894651239), ("BANK", "INDUSLAND BANK"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 6894651232), ("BANK", "CANARA BANK"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 6894651238), ("BANK", "HDFC BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 6894651231), ("BANK", "UCO BANK"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874314,
## 	    "FNAME" : "SACHIN KUMAR",
## 	    "LNAME" : "SAHU",
## 	    "FULL_ADDRESS" : "MANTRI ENCLAVES,RANCHI,JHARKHAND", 
## 	    "CITY/TOWN" : "RANCHI",
## 	    "STATE" : "JHARKHAND",
## 	    "PINCODE" : 834004,
## 	    "PHONE_NUMBER" : 8079075078,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 8946512340), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 8894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 8894651237), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 8894651232), ("BANK", "HDFC Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 8894651238), ("BANK", "PUNJAB NATIONAL BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 8894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874315,
## 	    "FNAME" : "SUBHO DEV",
## 	    "LNAME" : "ROY",
## 	    "FULL_ADDRESS" : "NEAR MACHII BAAZAR,BHORDHAMAN,WEST BENGAL", 
## 	    "CITY/TOWN" : "BORDHAMAN",
## 	    "STATE" : "WEST BENGAL",
## 	    "PINCODE" : 713103,
## 	    "PHONE_NUMBER" : 8899847036,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 4894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 4894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 4894651238), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 4894651237), ("BANK", "PUNJAB NATIONAL BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 4894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874316,
## 	    "FNAME" : "LALMOHAN",
## 	    "LNAME" : "KUMAR",
## 	    "FULL_ADDRESS" : "SHANJOG NAGAR,SAMASTIPUR,KHATIA,BIHAR", 
## 	    "CITY/TOWN" : "SAMASTIPUR",
## 	    "STATE" : "BIHAR",
## 	    "PINCODE" : 788741,
## 	    "PHONE_NUMBER" : 8248747076,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 2894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 2894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 2894651238), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 2894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874317,
## 	    "FNAME" : "SIDDHARTHA",
## 	    "LNAME" : "DAS",
## 	    "FULL_ADDRESS" : "NORTH DUMDUM,KOLKATA,WEST BENGAL", 
## 	    "CITY/TOWN" : "KOLKATA",
## 	    "STATE" : "WEST BENGAL",
## 	    "PINCODE" : 700019,
## 	    "PHONE_NUMBER" : 9847096023,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 3894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 3894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 3894651238), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 3894651239), ("BANK", "SYNDICATE Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 3894651238), ("BANK", "UCO BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 3894651231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874318,
## 	    "FNAME" : "SARVESH",
## 	    "LNAME" : "SINGH",
## 	    "FULL_ADDRESS" : "SINS CITY,BHOJPAI NAGAR,KATMANDU,NEPAL", 
## 	    "CITY/TOWN" : "KATMANDU",
## 	    "STATE" : "NEPAL",
## 	    "PINCODE" : 44600,
## 	    "PHONE_NUMBER" : 9938765597,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 1894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 1894651231), ("BANK", "BANK OF NEPAL"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874319,
## 	    "FNAME" : "SIDDHANT",
## 	    "LNAME" : "KEDIA",
## 	    "FULL_ADDRESS" : "NEAR JP EVENING COLLEGE,HILL TOWN,BHAWANIPATNA,KALAHANDHI,ODISHA", 
## 	    "CITY/TOWN" : "BHAWANIPATNA",
## 	    "STATE" : "ODISHA",
## 	    "PINCODE" : 713305,
## 	    "PHONE_NUMBER" : 8249847076,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 5894651234), ("BANK", "STATE BANK OF INDIA"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651239), ("BANK", "ICICI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651238), ("BANK", "AXIS BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651237), ("BANK", "IDBI Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651236), ("BANK", "PUNJAB NATIONAL BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651235), ("BANK", "ORIENTAL BANK OF COMMERCE"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651233), ("BANK", "SYNDICATE Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651232), ("BANK", "UCO BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 5894651231), ("BANK", "BANK OF BARODA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]},
##
## 	{   "UIN" : 316874320,
## 	    "FNAME" : "RAJAT",
## 	    "LNAME" : "SINGH",
## 	    "FULL_ADDRESS" : "NEAR JP EVENING COLLEGE,HILL TOWN,BHAWANIPATNA,KALAHANDHI,ODISHA", 
## 	    "CITY/TOWN" : "BHAWANIPATNA",
## 	    "STATE" : "ODISHA",
## 	    "PINCODE" : 766001,
## 	    "PHONE_NUMBER" : 8249847076,
## 	    "ACCOUNTS" : [
## 	    SON([("Account_no", 7899874234), ("BANK", "DENA BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7895647239), ("BANK", "UCO Bank"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7891544238), ("BANK", "CANARA BANK"), ("Account_type", "SAVINGS"),("AVAIL_BAL", 10000)]),
## 	    SON([("Account_no", 7898596231), ("BANK", "BANK OF INDIA"), ("Account_type", "CURRENT"),("AVAIL_BAL", 10000)])]}])
##
##
UIN_NO  = int(input("Enter your UIN NUMBER : "))

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
     db.DATA_CENTER.update(
          {'UIN' : UIN_NO,"ACCOUNTS.Account_no" : cookie[choose-1]},
          {"$set": {"ACCOUNTS.$.AVAIL_BAL" : amount},
           "$currentDate": {"lastModified": True}})
     
      

     
          
