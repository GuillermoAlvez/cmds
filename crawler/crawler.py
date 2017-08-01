#!/usr/bin/env python
import requests
import re

"""
import logging
import traceback
import re

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
"""


BASE_URL = "http://ubuntujs.labo:3010"

url = BASE_URL
#aca entra funcion crawler(url,url_antes,base) #url_antes no se si usarla


reUrls = re.compile(r'(?:src="|href=")(.*?)"')
print  url

try:
    r = requests.get(url)
except:
    pass


links = re.findall(reUrls,r.text)
if (links is not None): #(!vacio y estoy en el dominio), tengo que hacer una funcion que me diga si estoy en el dominio
	url_antes = url
	for i in range(0,len(links)):
		#aca verificar si es ruta relativa, absoluta, raiz						
		url = url_antes + "/" + links[i]
		print url














"""
if r.status_code == 200:
    content_length = len(r.text)
    available_paths.append(path + " - " + str(content_length))
elif r.status_code == 302 and "nodisponible" in r.headers["Location"]:
    unavailable_paths.append(path)
else:
    not_found_paths.append(path)



with open("output.txt", "w") as output:
    output.write("Recursos disponibles: \n\n")
    for path in available_paths:
	output.write(BASE_URL + path + "\n")

    output.write("\nRecursos existentes pero no disponibles:\n\n")
    for path in unavailable_paths:
	output.write(BASE_URL + path + "\n")

    output.write("\nRecursos no encontrados:\n\n")
    for path in not_found_paths:
	output.write(BASE_URL + path + "\n")

"""
