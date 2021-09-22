import requests
from PIL import Image
r = requests.get('https://api.github.com/events')
print(r.json())