# Importing Image class from PIL module
from PIL import Image

image = Image.open('./icons/delete.png')
new_image = image.resize((5, 5))
new_image.save('./icons/delete.png')
image = Image.open('./icons/update.png')
new_image = image.resize((5, 5))
new_image.save('./icons/update.png')