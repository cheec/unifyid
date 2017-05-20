import requests

import matplotlib.pyplot as plt
import numpy as np

def request_random(num):
    payload = {
    'num': num,
    'min': '0',
    'max': '255',
    'col': '1',
    'base': 10,
    'format': 'plain',
    'rnd': 'new'
    }

    req = requests.get('http://random.org./integers/', params=payload)
    return np.asarray([int(x) for x in req.text.split()])

if __name__ == "__main__":
    nx = ny = 128

    random_integers = request_random(str(nx * ny / 2))
    random_integers = np.append(random_integers, request_random(str(nx * ny / 2)))
    
    plt.plot(random_integers)
    plt.axis
    plt.show()
