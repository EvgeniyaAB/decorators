import requests
from decorators import logger


#task 1 -requests-http--
@logger
def superhero():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    resp = requests.get(url)
    resp_json = resp.json()
    heroes = ('Hulk', 'Captain America', 'Thanos')
    heroes_strenth = {}
    for num in resp_json:
        for hero in heroes:
            if hero == num['name']:
                heroes_strenth[num['name']] = num['powerstats']['intelligence']

    return max(heroes_strenth, key=heroes_strenth.get)

if __name__ == '__main__':
    superhero()