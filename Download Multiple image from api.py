from requests import get

KEY = '19223584-1678badef5331b34d39984671'
query = input('Enter your query: ').strip()
while ' ' in query:
    query = query.replace(' ', '+')
url = f'https://pixabay.com/api/?key={KEY}&q={query}&image_type=all&orientation=horizontal&per_page=9'

res = get(url)
large_image_url_list = []
if res.status_code == 200:
    data = res.json()
    images = data.get('hits')
    for image in images:
        large_image_url = image.get('largeImageURL')
        large_image_url_list.append(large_image_url)

i = 0
for large_image_url in large_image_url_list:
    res = get(large_image_url)
    if res.status_code == 200:
        content = res.content
        with open(f'images/polly-image-{str(i)}.jpg', 'wb') as f:
            f.write(content)
            i += 1
