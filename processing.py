from PIL import Image, ImageChops, ImageOps


# crop image only to non-empty data
def crop(img):
    bg = Image.new(img.mode, img.size, (255, 255, 255)) # create white image of the same size as img
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)

    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)

def resize(img):
    return img.resize((28, 28)) # mnist image size

def to_greyscale(img):
    return ImageOps.grayscale(img)

def process():
    img = Image.open("canvas.png")
    
    img = crop(img)
    img = resize(img)
    img = to_greyscale(img)
    img.show()

process()


