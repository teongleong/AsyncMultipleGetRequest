import asyncio
import aiofiles
import aiohttp

base_url = 'http://stats.nba.com/stats'
#HEADERS = {
#    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/45.0.2454.101 Safari/537.36'),
#}

async def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = f'{base_url}{endpoint}'
    print('Getting all players...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])

async def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = f'{base_url}{endpoint}'
    print(f'Getting player {player_name}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            print(resp)
            data = await resp.text()
    async with aiofiles.open(
            f'{player_name.replace(" ", "_")}.json', 'w') as file:
        await file.write(data)

#loop = asyncio.get_event_loop()
#player_args = []
#loop.run_until_complete(get_players(player_args))
#loop.run_until_complete(
#    asyncio.gather(
#        *(get_player(*args) for args in player_args)
#    )
#)


item_url_head = "https://us.api.battle.net/wow/item/"
item_url_tail = "?locale=en_US&apikey=a7z4utbr34kds8hrv7khf5qfzsu3u9tw"


async def get_item(id):
    blizz_url = item_url_head + str(id) + item_url_tail
    async with aiohttp.ClientSession() as session:
        async with session.get(blizz_url) as resp:
            print(resp)
            data = await resp.text()
            print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_item(144457))




async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


