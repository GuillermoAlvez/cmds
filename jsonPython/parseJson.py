#!/usr/bin/env python
import requests
import json
import time

users = {"Usuarios": [  {"nombre":"Artur","puerto":"3000"}  ,
			{"nombre":"Facha","puerto":"3001"}  ,
			{"nombre":"Cacho","puerto":"3002"}  ,
			{"nombre":"Pipe","puerto":"3003"}  ,
			{"nombre":"Anakatana","puerto":"3004"}  ,
			{"nombre":"Anto","puerto":"3005"}  ,
			{"nombre":"Matiew","puerto":"3006"}  ,
			{"nombre":"Pollo","puerto":"3007"}  ,
			{"nombre":"Yorge","puerto":"3008"}  ,
			{"nombre":"Nandow","puerto":"3009"}  ,
			{"nombre":"Norbert","puerto":"3010"}  ,
			{"nombre":"Nowel","puerto":"3011"}  ,
			{"nombre":"Flores","puerto":"3012"}  ]}
jsonUsers = json.dumps(users)
jsonDecode = json.loads(jsonUsers)

#print("\nusuario : "+ jsonDecode["Usuarios"][i]["nombre"])
print("MONO , PUNTAJE;")
for i in range (0,13):
	

	puerto = jsonDecode["Usuarios"][i]["puerto"]
	#print()
	req=''
	while req == '':
		try:
			req = requests.get("http://ubuntujs.labo:"+ puerto +"/api/Challenges")
		except:
			#print("Connection refused by the server..")
			#print("Let me sleep for 5 seconds")
			#print("ZZzzzz...")
			time.sleep(5)
			#print("continua...")
			continue


	r= req.json()
	suma = 0
	for challenge in range (0,37):
		dificultad = r["data"][challenge]["difficulty"]
		resuelto = r["data"][challenge]["solved"] == True
		#print (resuelto)
		if resuelto:
			suma = suma + dificultad
	print(jsonDecode["Usuarios"][i]["nombre"] + "," + str(suma))



