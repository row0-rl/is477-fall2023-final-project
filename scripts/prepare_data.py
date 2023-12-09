import requests
import os
import hashlib
from zipfile import ZipFile


if not os.path.exists('../data'):
    os.mkdir('../data')


url = "https://archive.ics.uci.edu/static/public/73/mushroom.zip"
sha256 = 'face32f32647e0d939f6233f36dd30dd5d619ae9f3f9b8e10bea4ac7e1f60b1a'
exists = False


response = requests.get(url)
filepath = '../data/mushroom.zip'
if os.path.exists(filepath):
    with open(filepath, mode='rb') as f:
        data = f.read()
    if (hashlib.sha256(data).hexdigest() == sha256):
        exists = True
if not exists:
    with open(filepath, mode='wb') as f:
        f.write(response.content)
    with open(filepath, mode='rb') as f:
        data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    assert sha256 == sha256hash

with ZipFile(filepath, mode='r') as f:
    f.extractall('../data')
    