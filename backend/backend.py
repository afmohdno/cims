from flask import Flask, request, jsonify
from flask_cors import CORS
from functions.data_handler import *
from data.config import *
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_SORT_KEYS"] = False
CORS(app, resources={r"/*":{"origins": "*"}})

# check server running
@app.route("/")
def status():
	return { "status": "running" }

# get list of all customers
@app.route("/customers")
def getall_customers():
	res = getall_cust()
	return res

# get single customer
@app.route("/customer/<cust_id>")
def get_customer(cust_id):
	_id = ObjectId(cust_id)
	res = get_cust(_id)
	return res

# add single customer
@app.route("/customer", methods=["POST"])
def add_customer():
	post_data = request.get_json()
	print("post_data", post_data)
	customer = {
		"name": post_data.get("name"),
		"email": post_data.get("email"),
		"city": post_data.get("city"),
		"age": post_data.get("age")
	}
	same_email = check_email(customer["email"])
	if same_email:
		res = { "status": "failed", "message": "Email already exists"}
	else:
		res = add_cust(customer)
	return res

# update single customer
@app.route("/customer/<cust_id>", methods=["PUT"])
def update_customer(cust_id):
	update_data = request.get_json()
	print("update_data",update_data)
	customer = {
		"name": update_data["name"],
		"email": update_data["email"],
		"city": update_data["city"],
		"age": update_data["age"]
	}
	print(cust_id, customer)
	res = update_cust(cust_id,customer)
	return res

# delete single customer
@app.route("/customer/<cust_id>", methods=["DELETE"])
def delete_customer(cust_id):
	res = delete_cust(cust_id)
	return res

if __name__ == "__main__":
	app.run(debug=True)