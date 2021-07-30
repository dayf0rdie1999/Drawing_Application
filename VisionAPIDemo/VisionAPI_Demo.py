import os, io
from google.cloud import vision
from google.cloud.vision import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'D:\Drawing Application\VisionAPIDemo'
IMAGE_FILE = 'myDrawing.png'

FILE_PATH = os.path.join(FOLDER_PATH,IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content = content)
vision = client.document

