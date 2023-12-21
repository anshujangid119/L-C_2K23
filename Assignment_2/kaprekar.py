import requests
from PIL import Image
from io import BytesIO

def get_pexels_images(api_key, query, num_images=5):
    url = f'https://api.pexels.com/v1/search?query={query}&per_page={num_images}'
    headers = {'Authorization': api_key}

    response = requests.get(url, headers=headers)
    data = response.json()

    images = []
    for photo in data.get('photos', []):
        images.append(photo['src']['large'])

    return images

def create_image_collage(images, output_path='collage.jpg'):
    images_data = [Image.open(BytesIO(requests.get(image).content)) for image in images]

    # Calculate collage size based on the first image
    collage_width = images_data[0].width * len(images)
    collage_height = images_data[0].height

    # Create a new image with the calculated size
    collage = Image.new('RGB', (collage_width, collage_height))

    # Paste each image into the collage
    x_offset = 0
    for img in images_data:
        collage.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save the collage
    collage.save(output_path)
    collage.show()

if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with your actual Pexels API key
    api_key = 'lMHAs8u41325vhL5vEiH0l8MjiRxhuQ8wP8D7uNVVJ9dTnKlVAXLwUuj'
    query = 'nature'  # Replace with your desired query
    num_images = 5

    images = get_pexels_images(api_key, query, num_images)
    create_image_collage(images)
