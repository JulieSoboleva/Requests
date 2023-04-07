import requests


def get_heroes_data():
    heroes_url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(heroes_url)
    return response.json()


if __name__ == '__main__':
    data = get_heroes_data()
    dict_intell = {}
    for hero in data:
        if hero['name'] in ('Hulk', 'Captain America', 'Thanos'):
            dict_intell[hero['powerstats']['intelligence']] = hero['name']

    res = sorted(dict_intell.items(), reverse=True)
    print('Самый умный супергерой:', res[0][1])
