import json

item_id_file_name = "data/item-name-id.txt"


data_file_list = [
]

data_file_list2 = [
    "itemdata-144001-145000.txt",
    "itemdata-145001-146000.txt", 
    "itemdata-146001-147000.txt", 
    "itemdata-147001-148000.txt", 
    "itemdata-148001-149000.txt",
    "itemdata-149001-150000.txt",
    "itemdata-150001-151000.txt",
    "itemdata-151001-152000.txt",
    "itemdata-152001-153000.txt",
    "itemdata-153001-154000.txt",
    "itemdata-154001-155000.txt",
    "itemdata-155001-156000.txt",
    "itemdata-156001-157000.txt",
    "itemdata-157001-158000.txt",
    "itemdata-158001-159000.txt",
    "itemdata-159001-160000.txt",
    "itemdata-160001-161000.txt",
    "itemdata-161001-162000.txt",
    "itemdata-162001-163000.txt",
    "itemdata-163001-164000.txt",
    "itemdata-164001-165000.txt",
    "itemdata-165001-166000.txt"
]

for i in range(0,144):
    data_file_list.append("itemdata-"+str(i*1000)+"-"+str(i*1000+999)+".txt")

#for i in range(0, 144):
#    print(data_file_list[i])

for filename in data_file_list2:
    data_file_list.append(filename)

for filename in data_file_list:
    print(filename)

# delete all content of the file
def clear_file(infile):
    infile.seek(0)
    infile.truncate(0)

item_id_file = open(item_id_file_name, "r+", encoding='utf8')
clear_file(item_id_file)

for fileName in data_file_list:
    item_data_file = open("data/" + fileName, "r", encoding='utf8')
    x = None
    while (True):
        x = item_data_file.readline()
        if x != "":
            #print(x)
            json_data = json.loads(x)
        else:
            break
        print(json_data["name"])
        item_id_file.write(json_data["name"]+'\t'+str(json_data["id"])+'\n')

item_id_file.close()
item_data_file.close()
