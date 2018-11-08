import requests
import json

#print("")
#parsed_json = json.loads(r.content)
#print(parsed_json['name'])

#empty_count = 0

f = open("demofile.txt", "a", encoding='utf8')

item_url_head = "https://us.api.battle.net/wow/item/"
item_url_tail = "?locale=en_US&apikey=a7z4utbr34kds8hrv7khf5qfzsu3u9tw"

arr = []
#arr_index = 0

print("requesting...")
count = 147501
for i in range(count, 148001):
	r = requests.get(item_url_head + str(i) + item_url_tail)
	#print(r.status_code)
	#print("")
	#print(r.headers)
	#print("")
	#print(r.content)
	#print("")
	if (r.status_code == 404):
		continue
	
	parsed_json = json.loads(r.content)
	arr.append(parsed_json)
	print(parsed_json['id'])
	#arr_index += 1
	#print(parsed_json['name'])
	#print(str(parsed_json['id']) + parsed_json['name'])
#	f.write(json.dumps(parsed_json)+'\n')

	#json.dump(parsed_json, f)
	#f.write("\n")

print("writing...")
for j in arr:
	json.dump(j, f)
	f.write("\n")
