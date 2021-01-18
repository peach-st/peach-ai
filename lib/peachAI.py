import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time
import random

cred = credentials.Certificate("peach-ai.json")

firebase_admin.initialize_app(cred, {
	'databaseURL':"https://peach-ai-default-rtdb.firebaseio.com"
	})

database =db.reference('')

def x000001(response, db):
	save = database.child("OBU")
	lk = db["OBU"]["response"]
	lk += [response]	
	print(lk, response, db)
	save.update({
		"response": lk
		})
def x000002(js):
	db = database.get()
	otvet = db["ai"]
	try:
		otvet = otvet[js["response"]]
		return(otvet)
	except:
		x000001(js["response"], db)
		return("NONE-BASE-DATA")


def get(response):
	return(x000002({"response":response}))
