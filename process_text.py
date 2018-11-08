#with open("log.txt") as infile:
#    for line in infile:
#        do_something_with(line)

import sys

sys.path.append('./bigjson/')
import bigjson

with open('auction-130001112018.json', 'rb') as f:
    j = bigjson.load(f)
    element = j[4]
    print(element['type'])
    print(element['id'])
