import requests

payload = {'num': '10', 'min': '1', 'max': '6', 'col': '1', 'base': 10, 'format': 'plain', 'rnd': 'new'}
req = requests.get('http://random.org./integers/', params=payload)

random_integers = [int(x) for x in req.text.split()]

