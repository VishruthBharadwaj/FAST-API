from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
import json



db=[]
import requests

class City(BaseModel):
	name:str
	timezone:str
class Employee(BaseModel):
	name:str
	age:int
	salary:int
	id:int


@app.get('/')
def index():
	return {'key' : 'value'}

@app.get('/cities')
def get_cities():
	results = []
	for city in db:
		r=requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
		current_time = r.json()['datetime']
		
		results.append({'name': city['name'], 'timezone':city['timezone'], 'current_time':current_time})
	return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
	city=db[city_id-1]
	r=requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
	current_time = r.json()['datetime']
	return {'name': city['name'], 'timezone':city['timezone'], 'current_time':current_time}

@app.get('/employee')
def get_employee():
	results = []
	r=requests.get(f'http://dummy.restapiexample.com/api/v1/employees')
	current = r.json().get('data')
	print(current)
	return current

@app.post('/employee')
def create_employee(employee:Employee):
	print(employee)

	#r = requests.post(f'http://dummy.restapiexample.com/api/v1/create' ,json=json.dumps(employee, default=json_util.default))
	#current = r.json().get('data')
	#print(current)
	#return current
	db.append(employee.dict())
	return db[-1]

@app.post('/cities')
def create_city(city:City):
	db.append(city.dict())
	return db[-1]
@app.delete('/cities/{city_id}')

def delete_city(city_id: int):
	db.pop(city_id-1)
	return {}