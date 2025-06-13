from requests import get

API_KEY = 'EocUeWFOhWLK5NgillADzcBhLnjrT5UDIizpT3rYO2RrTuzBKkYqkR2P'
query = input('Enter your query: ').strip()
if ' ' in query:
    query = query.replace(' ', '+')
per_page = 5
headers = {'Authorization': API_KEY}
params ={'query': query, 'per_page': per_page}
res = get('https://api.pexels.com/v1/search', headers=headers, params=params)
original_photo_list = []
if res.status_code == 200:
    data = res.json()
    photos = data.get('photos')
    for photo in photos:
        original_photo_url = photo.get('src').get('original')
        original_photo_list.append(original_photo_url)

i = 0
for original_photo_url in original_photo_list:
    res = get(original_photo_url)
    if res.status_code == 200:
        content = res.content
        with open(f'images/bollywwod-hot{str(i)}.jpg', 'wb') as kk:
            kk.write(content)
    i += 1
