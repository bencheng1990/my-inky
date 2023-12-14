from inky.auto import auto
from PIL import Image


def display(image):
    inky = auto(ask_user=True, verbose=True)
    resized_image = Image.open(image).resize(inky.resolution)
    inky.set_image(resized_image, saturation=0.5)
    inky.show()
