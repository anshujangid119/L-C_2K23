import requests
from PIL import Image
from io import BytesIO

def get_pexels_images(api_key, query, num_images):
    url = f'https://api.pexels.com/v1/search?query={query}&per_page={num_images}'
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    images = []
    for photo in data.get('photos', []):
        images.append(photo['src']['large'])
        # print("image", images)
    return images

def create_image_collage(images, output_path='collage.jpg'):
    images_data = [Image.open(BytesIO(requests.get(image).content)) for image in images]
    collage_width = images_data[0].width * len(images)
    collage_height = images_data[0].height
    collage = Image.new('RGB', (collage_width, collage_height))
    x_offset = 0
    for img in images_data:
        collage.paste(img, (x_offset,100))
        x_offset += img.width

    # Save the collage
    collage.save(output_path)
    collage.show()

if __name__ == '__main__':
    api_key = 'lMHAs8u41325vhL5vEiH0l8MjiRxhuQ8wP8D7uNVVJ9dTnKlVAXLwUuj'
    query = 'coding'
    num_images = 5
    images = get_pexels_images(api_key, query, num_images)
    create_image_collage(images)
