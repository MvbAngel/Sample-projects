import json
from urllib import request
from pathlib import Path

filename = 'charles.json'

class Forfatter:

    def __init__(self, navn, aliases, url, artikler):
        self.navn = navn
        self.alias = aliases
        self.url = url
        self.artikler = artikler

    def skriv(self):
        print(f'Navn: {self.navn}, alias: {self.alias}, \
                URL: {self.url}, antall artikler: \
                {len(self.artikler)}')

def fetch(author_id):
    '''
    Henter informasjon om author_id
    lagrer til json-fil author_id.json
    returnerer data (dict)
    '''
    api = 'http://api.semanticscholar.org/v1/author/'
    filename = author_id + '.json'

    if not Path(filename).exists():
        api_endpoint = api + author_id
        response = request.urlopen(api_endpoint)
        data = json.loads(response.read())
        with open(filename, 'w') as file:
            json.dump(data, file)
    else:
        with open(filename) as file:
            data = json.load(file)
    return data

def get_author(author_id):
    data = fetch(author_id)
    charles = Forfatter(
        data['name'],
        data['aliases'],
        data['url'],
        data['papers']
    )

    forfatter = {
        'navn': data['name'],
        'alias': data['aliases'],
        'url': data['url'],
        'artikler': sorted(data['papers'], key=lambda elem: elem['year'])
    }

    for key, value in forfatter.items():
        if key == 'artikler':
            print(key, len(value))
            for artikkel in value:
                print(f"({artikkel['year']}) {artikkel['title']}")
        else:
            print(key, value)

if __name__ == '__main__':
    get_author('145009961')

