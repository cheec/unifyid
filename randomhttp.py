import requests

import matplotlib.pyplot as plt
import numpy as np

def request_random(num, min_val, max_val):
    payload = {
        'num': str(num),
        'min': str(min_val),
        'max': str(max_val),
        'col': '1',
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }
    
    req = requests.get('https://www.random.org/integers/', params=payload)
    if req.status_code != 200: # TODO: quota checking before polling
        print('Error requesting bits. (' + str(req.status_code) + ')')
        exit(1)
        
    return np.asarray(int(x) for x in req.text.split())

nx = ny = 128
min_rgb = 0
max_rgb = 2 ** 24 - 1 # rgb hex (6 bytes)

if __name__ == "__main__":
    random_rgb = request_random(nx * ny / 2, min_rgb, max_rgb)
    random_rgb = np.append(random_rgb, request_random(nx * ny / 2, min_rgb, max_rgb))

    random_rgb = random_rgb.reshape(128, 128)

    fig = plt.imshow(random_rgb)
    fig.set_cmap('jet')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()

