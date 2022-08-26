import json
from bson import ObjectId
from data.config import *

class JSONEncoder(json.JSONEncoder):
	def default(self,o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self,o)

def getall_cust():
	data = list(db.testdb.find())
	return JSONEncoder().encode(data)

def get_cust(_id):
	return JSONEncoder().encode(db.testdb.find_one({"_id":_id}))

def add_cust(cust_data):
	result = db.testdb.insert_one(cust_data)
	if result.inserted_id:
		return { "status": "success", "message": "Customer added"}
	else:
		return { "status": "failed", "message": "Customer not added"}

def update_cust(_id,data):
	print("updating customer")
	result = db.testdb.update_one({"_id":ObjectId(_id)},{"$set":data})
	if result.matched_count > 0:
		return { "status": "success", "message": "Customer updated"}
	else:
		return { "status": "failed", "message": "Customer not updated"}

def delete_cust(_id):
	result = db.testdb.delete_one({"_id":ObjectId(_id)})
	if result.deleted_count > 0:
		return { "status": "success", "message": "Customer deleted"}
	else:
		return { "status": "failed", "message": "Customer not deleted"}

def check_email(email):
	entry = db.testdb.find_one({"email":email})
	if entry:
		return True
	else:
		return False