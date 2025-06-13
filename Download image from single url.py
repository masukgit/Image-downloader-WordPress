from requests import get

url = 'https://pixabay.com/get/g62cc8bca60d088bd6969973813673a0c821832e1d8caf281f2e2440670921f5c73b963ff5a6933e4ebb94fd8194206d917db9ec488cd687e3fa1e15233bfe8c3_640.jpg'
res = get(url)
if res.status_code == 200:
    content = res.content
    with open('amar image.jpg', 'wb') as f:
        f.write(content)

