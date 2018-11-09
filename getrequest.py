import requests
import json
import time
import datetime

# r = requests.get("https://us.api.battle.net/wow/character/frostmourne/Blindasfox?locale=en_US&apikey=a7z4utbr34kds8hrv7khf5qfzsu3u9tw")

r = requests.get("https://us.api.battle.net/wow/auction/data/frostmourne?locale=en_US&apikey=a7z4utbr34kds8hrv7khf5qfzsu3u9tw")

print(r.status_code)
print("")
print(r.headers)
print("")
print(r.content)

print("")
parsed_json = json.loads(r.content)
print(parsed_json)

print("")
modTime = parsed_json['files'][0]['lastModified']
fileURL = parsed_json['files'][0]['url']
print(modTime)
print(1284105682)
print(fileURL)

#15415 54200000
#15415 61340000


from datetime import datetime
#ts = int(modTime)

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.fromtimestamp(int("1284105682")).strftime('%Y-%m-%d %H:%M:%S'))

import urllib.request

#print('Beginning file download with urllib2...')

#srcPath = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'  
srcPath2 = fileURL
#destPath = 'C:/Users/teongleong/Downloads/cat.jpg'
datetime_string = datetime.now().isoformat(timespec='minutes')
datetime_string = datetime_string.replace(":", "-")
print(datetime_string)
destPath2 = 'C:/Users/teongleong/Downloads/' + str(modTime) + '-' + datetime_string + '.json'
	
import os.path
if (not os.path.exists(destPath2)): 
	print("New file, proceed to download")
	urllib.request.urlretrieve(srcPath2, destPath2) 
	print("done")
else:
	print("No new file")
