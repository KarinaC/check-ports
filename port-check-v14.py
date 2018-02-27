## Port check contra Marathon
## Creado en Febrero 2018
## Por: Karina Costa (RedBee)
## V14
## usage: python3 port-check-v14.py --ports 18081 --marathon http://localhost:18082
################################

#######################
#Importo las librerias
#######################
import json
import requests
import argparse

################################################
#Defino parametros a ser ingresados por el user
################################################
parser = argparse.ArgumentParser()
parser.add_argument('--ports', type=int, help='Puerto/s a chequear')
parser.add_argument('--marathon', type=str, default='localhost:8080', help='marathon a revisar')
args = parser.parse_args()



#def Checklink():
#	if args.marathon




#####################################
#Creo la función que hara el chequeo
#####################################
def consultapuertos():
	r = requests.get(args.marathon + "/v2/apps") #de esta forma el user solo ingresa la url de marathon --marathon http://localhost:18082
	rformat = r.json()
	serviport = [] #lista vacia a la que se le van appendear los puertos obtenidos mas abajo
	name = []
	todos = {}
	apps = rformat.get('apps') #me traigo el APPS completo
	for item in apps:
		ids=item.get('id') #me traigo los ids
		con = item.get('container') #me traigo el dict de container
		try:
			pm = con.get('docker').get('portMappings') #me traigo los docker que tengan PORTMAPPING
			if pm is not None:
				for po in pm:
					todos[po.get('servicePort')] = ids #armo dict poniendo servicePort como key
			else:
				print("El servicio " + "\"" + (ids)  + "\"" + " no tiene portMappings, Network seteado como HOST")
		except AttributeError:
		    pass
	print("")
	print("")
	#print(todos)   #estaba probando si traia lo deseado


	if args.ports in todos:
		print("--Chequeo del puerto--")
		print("CUIDADO! el puerto esta en uso por " + "\"" + todos.get(args.ports) + "\"")
	else:
		print("--chequeo del puerto--")
		print("puerto libre")

if __name__ == '__main__':


    consultapuertos()





