#!/usr/bin/env python
import requests
import json
import time
import re

#print("\nusuario : "+ jsonDecode["Usuarios"][i]["nombre"])

for i in  range(97,123):
	for j in  range( 97,123): 
		for k in  range( 97,123):
			a=(hex(i)[2]+hex(i)[3]).decode("hex")  
			b=(hex(j)[2]+hex(j)[3]).decode("hex")
			c=(hex(k)[2]+hex(k)[3]).decode("hex")		
		
			req = requests.get("http://ubuntujs.labo:3010/i18n/"+a+b+c+".json")
			time.sleep(1)
			tiempo = req.text
			regex = re.compile(r'INVALID_PASSWORD_LENGTH')
			links = re.search(regex,req.text)
			if links is not None:
				print("http://ubuntujs.labo:3010/i18n/"+a+b+c+".json")
		
