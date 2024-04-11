import requests
import random

images = ['https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png', 'https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg', 'https://images.ctfassets.net/2y9b3o528xhq/5p7HANmA1jsw8P9EVOeVso/cbfa17357399d99a76d641c777e81a81/self-paced.png']

for each_url in images:
    r = requests.get(each_url)
    file_name = f'./tmp/{random.randint(1, 10000000)}.png'
    with open(file_name, 'wb') as f:
        f.write(r.content)
        print('Saved ' + file_name)
    f.close()
    r.close()