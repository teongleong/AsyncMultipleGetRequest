import time, threading
from subprocess import call

def foo():
	print(time.ctime())
	call(["python", "./getrequest.py"])
	threading.Timer(60*30, foo).start()

foo()
