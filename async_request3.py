# modified fetch function with semaphore
import random
import asyncio
import json
import concurrent
from aiohttp import ClientSession

data_dict = {}

async def fetch(url, session):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        status = response.status
        #print("{}:{} with delay {}".format(date, response.url, delay))
        #print("status: {}\n".format(status))
        if status == 200:
            return await response.read()
        elif status == 404:
            return None
        elif status == 403:
            error_msg = {'url': url, 'status': 403}
            json_str = json.dumps(error_msg)
            return json_str


async def bound_fetch(sem, url, id, session):
    # Getter function with semaphore.
    async with sem:
        data = await fetch(url, session)
        if (data != None):
            parsed_json = json.loads(data)
            data_dict[id] = parsed_json
        #print(parsed_json)
        #print("")

item_url_head = "https://us.api.battle.net/wow/item/"
item_url_tail = "?locale=en_US&apikey=a7z4utbr34kds8hrv7khf5qfzsu3u9tw"


async def run(start, end):
    
    f = open("data/itemdata-{}-{}.txt".format(start, end-1), "a", encoding='utf8')
    #url = "http://localhost:8080/{}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)
    #start = 149001  # 147360
    #end = 150001
    incr = 10

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        print("start {}, end {}".format(start, start+incr))
        #print("check {}".format(start+incr < end))
        while start + incr <= end:
            data_dict.clear()
            for i in range(start, start + incr): # 8800 8900
                url = item_url_head + str(i) + item_url_tail
                # pass Semaphore and session to every GET request
                task = asyncio.ensure_future(
                    bound_fetch(sem, url, i, session))
                tasks.append(task)
                
           
            responses = asyncio.gather(*tasks)
            await responses
            start += incr

            for key in sorted(data_dict):
                #print("{}: {}".format(key, data_dict[key]))
                print(key)
                #print("")
                #for j in arr:
                json.dump(data_dict[key], f)
                f.write("\n")
            await asyncio.sleep(1)
    f.close()

#loop = asyncio.get_event_loop()

range_incr = 1000
range_start = 143000
range_end = 144000

while range_start + range_incr <= range_end:
    print("Started " + str(range_start))
    
    #asyncio.new_event_loop()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(range_start, range_start + range_incr))

    executor = concurrent.futures.ThreadPoolExecutor(5)
    loop.set_default_executor(executor)
    try:
        #loop.run_until_complete(main())
        loop.run_until_complete(future)
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        # see: https://stackoverflow.com/a/32615276/1113207
        executor.shutdown(wait=True)
        #loop.close()

    print("Done " + str(range_start))
    range_start += range_incr

#async def periodic():
#    while True:
#        print("loop")
#        await asyncio.sleep(1)

#def stop():
#    task.cancel()

#loop.call_later(3, stop)
#task = loop.create_task(periodic())

#try:
#    loop.run_until_complete(task)
#except asyncio.CancelledError:
#    pass
