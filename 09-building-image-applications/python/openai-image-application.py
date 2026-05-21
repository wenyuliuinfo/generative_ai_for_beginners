# Import Libraries
import os
import requests
import base64
from requests.exceptions import RequestException
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

# Configure DeepSeek as used LLM
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        model="gpt-image-2-vip",
        prompt="A cat in a sunny playground with food in front",
        size="1024x1024"
    )
    image_dir = os.path.join(os.curdir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path
    image_path = os.path.join(image_dir, 'generated-image.png')
    #print(generation_response.data[0])

    #image_url = generation_response.data[0].url
    image_b64 = generation_response.data[0].b64_json    
    #print(image_url)
    if image_b64.startswith('data:image/png;base64,'):
        image_b64 = image_b64.replace('data:image/png;base64,', '')


    # Add timeout and error handling for HTTP request
    '''
    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        generated_image = response.content
    except RequestException as req_err:
        print(f"Failed to download generated image: {req_err}")
        raise

    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)
    '''

    image_data = base64.b64decode(image_b64)
    image = Image.open(BytesIO(image_data))
    image.save(image_path)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

except OpenAIError as err:
    print(f"OpenAI API error: {err}")