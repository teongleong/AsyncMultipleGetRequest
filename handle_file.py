import json 
import itemID
from itemID import *

fileHandle = open("C:/Users/teongleong/Downloads/1541561340000.json",mode="r", encoding="utf8")
content = fileHandle.read()
parsed_json = json.loads(content)

tmplst = []

# filter for arcane crystals
for auc in parsed_json["auctions"]:
	if auc["item"] == get_id("Arcane Crystal"):
		tmplst.append(auc)
	
#print the results out
for auc in tmplst:
	print(auc)
	
print(len(tmplst))