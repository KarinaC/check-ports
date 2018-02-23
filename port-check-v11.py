##Port check on Marathon
## Created February 21, 2018
## creator Karina Costa
###############################

#####################
#Librerias a utilizar
#####################
import json
import requests



r = requests.get('http://localhost:18082/v2/apps/')
rformat = r.json()
newport = 10004

#Del dict completo, me traigo la key APPS
apps = rformat.get('apps')
for item in apps:
	ids=item.get('id')
	con = item.get('container')
	try:
		pm = con.get('docker').get('portMappings')
		if pm is not None:
			print("Docker con PortMappings: " + "\"" + ids + "\"")
			#print(pm)
			for po in pm:
				ports=po.get('servicePort')
				print(ports)
				if str(newport) not in str(ports):
					print("puerto libre, usalo nomas")
				else:
					print("EPA EL PUERTO ESTA EN USO LOCOOO, BUSCATE OTRO")
		else:
			print("Docker" + "\"" + ids  + "\"" + " tien el Network seteado como HOST, no tiene portMappings")
	except AttributeError:
	    pass
	#print(puertos)
	print("")





## FORMA INVERSA NO TAN CORRECTA
	#try:
		#pm = con.get('docker').get('portMappings')
		#if pm is None:
			#print("Network seteado como HOST, no tiene portMappings")
			##print(item)
			##print("")
		#else:
			#print("Este docker tiene PortMappings: " + ids)
			#print(pm)
	#except AttributeError:
		#pass
	#print("")



