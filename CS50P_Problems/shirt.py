import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_filename, input_extension = os.path.splitext(sys.argv[1])
output_filename, output_extension = os.path.splitext(sys.argv[2])

if input_extension.lower() not in (".jpg",".jpeg", ".png"):
    sys.exit("Invalid input")
if output_extension.lower() not in (".jpg",".jpeg", ".png"):
    sys.exit("Invalid output")
if input_extension.lower() != output_extension.lower():
    sys.exit("Input and output have different extension")

try:
    with Image.open(sys.argv[1]) as photo:
        shirt = Image.open("shirt.png")
        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
     
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")