import requests
import json

base_url = 'https://execross.com/api/v3'
apikey = 'forexecman'
session = requests.Session()
session.headers.update({'apikey': apikey})

# Use image path
files = [
    ('images', ('image1.jpg', open('assets/cobrax.jpg', 'rb'), 'image/jpeg')),
    ('images', ('image2.jpg', open('assets/th.jpeg', 'rb'), 'image/jpeg'))
]

"""
# If want empty files and use only url

files = []
"""

# Use Image URL
data = {
    'urls': json.dumps([
        'https://images.nightcafe.studio/jobs/g9k7ET6X4eTnJMIASD9Q/g9k7ET6X4eTnJMIASD9Q--1--83vb5.jpg',
        'https://img.freepik.com/premium-photo/3d-rendering-arabian-cobra-animal-ai-generative_842224-8185.jpg'
    ])
}

"""
# If want empty url and use only file path

data = {
    'urls': json.dumps([])
}
"""
saveimageAs = "assets/combined_img.jpg"
response = session.post(f"{base_url}/combine", files=files, data={'urls': data['urls']})
if response.status_code == 200:
    with open(f'{saveimageAs}', 'wb') as f:
        f.write(response.content)
    print(f'Image successfully saved as: {saveimageAs}')
else:
    print(f'Failed to combine images. Status code: {response.status_code}')
    print(response.text)





