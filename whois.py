import pythonwhois
import sys
import json

asdf = open(sys.argv[1],'r')
a = asdf.readline()
asdf.close()

data = pythonwhois.get_whois(a)
def data_handler(obj):#this funciton in order to catch timeerror
	if hasattr(obj, 'isoformat'):
		return obj.isoformat()
	else:
		raise TypeError

jsonString = json.dumps(data, default = data_handler)

wasd = open('jsonfile','w')
wasd.write(jsonString)

wasd.close()
