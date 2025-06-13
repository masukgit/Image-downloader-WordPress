from requests import get

KEY = '19223584-1678badef5331b34d39984671'
query = input('Enter your query: ')
while ' ' in query:
    query = query.replace(' ', '+')
# url = f'https://pixabay.com/api/?key={KEY}&q={query}&image_type=photo'
# url = f'https://pixabay.com/api/?key={KEY}&q={query}&image_type=all'
url = f'https://pixabay.com/api/?key={KEY}&q={query}&image_type=all&orientation=horizontal&per_page=3'
res = get(url)
if res.status_code == 200:
    data = res.json()
    images = data.get('hits')

for image in images:
    print(image.get('webformatURL'))

