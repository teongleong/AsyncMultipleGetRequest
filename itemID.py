import re
import pprint

item_id_file = open("data/item-name-id-09-nov.txt", "r+", encoding='utf8')

id2Name = {}
name2ID = {}

#content2 = item_id_file.readline()
#print(content2)

for line in item_id_file:
#   print(line)
	m = re.search(r'^(.*)\t(\d+)$', line)
	name = m.group(1)
	id = int(m.group(2))
	id2Name[id] = name
	name2ID[name] = id
	#print(m.group(1))
	#print(m.group(2))
	#if '20' in line:
	#	break
	
#print(id2Name["80"])
#print(name2ID["Soft Fur-Lined Shoes"])

def get_name(id):
	return id2Name[id]
	
def get_id(name):
	return name2ID[name]

#pp = pprint.PrettyPrinter(indent=4)


	
item_id_file_json = open("data/itemid-name-09-nov.json", "w", encoding='utf8')
pprint.pprint(id2Name, item_id_file_json)
