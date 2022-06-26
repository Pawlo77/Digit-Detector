from PIL import Image, ImageChops, ImageOps
from tensorflow import keras
import numpy as np


class Predictor:
    model = keras.models.load_model("model.h5")

    def predict(self, img_name):
        try:
            img = Image.open(img_name)    
            img = self.to_greyscale(img)
            img = self.crop(img)
            img = self.resize(img)
            img.show()
            img = np.asarray(img)
            img = img[np.newaxis, :, :, np.newaxis]
            
            prediction = self.model.predict(img)
            prediction = self.decode_label(prediction)
        except:
            return "Wrong data provided"
        else:
            return str(prediction)

    # crop image only to non-empty data
    def crop(self, img):
        bg = Image.new(img.mode, img.size, 255) # create white image of the same size as img
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)

        bbox = diff.getbbox()
        if bbox:
            return img.crop(bbox)

    def resize(self, img):
        return img.resize((28, 28)) # mnist image size

    def to_greyscale(self, img):
        img = ImageOps.grayscale(img)
        pixels = img.load()

        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if pixels[x, y] != 255:
                    pixels[x, y] = 0
        return img

    def decode_label(self, one_hots):
        return np.argmax(one_hots)


predictor = Predictor()