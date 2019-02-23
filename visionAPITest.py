import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instatiates a client
client = vision.ImageAnnotatorClient()

# The name of the image fie to annotate
file_name = os.path.join(os.path.dirname(__file__),
        'businessCard.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs text detection on the image file
result = client.text_detection(image=image)
texts = result.text_annotations

print('Text:')
for text in texts:
    print(text)
