import urllib.request
import os

assets_dir = './assets'
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

images = ['p1.jpg', 'p2.jpg', 'p3.jpg', 'p4.jpg']
base_url = 'https://shadowthief.netlify.app/'

for img in images:
    url = base_url + img
    dest = os.path.join(assets_dir, img)
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"Downloaded {img}")
    except Exception as e:
        print(f"Failed to download {img}: {e}")
