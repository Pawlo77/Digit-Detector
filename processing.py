from tensorflow import keras
import numpy as np
import cv2
import os


model_name = "model1.h5"

class Predictor:
    model = keras.models.load_model(model_name)
    padding = 30
    id_ = 0
    save_ = False

    def predict(self, stream):
        try:
            img_array = np.asarray(bytearray(stream.read()), dtype="uint8")
            img_array = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            img_array = self.preprocess(img_array)

            if self.save_:
                self.save(img_array)
            
            img_array = img_array[np.newaxis, ..., np.newaxis]
            prediction = self.model.predict(img_array)
            prediction = self.decode_label(prediction)
        except Exception as e:
            print(e)
            return "Wrong data provided"
        else:
            return str(prediction)

    def preprocess(self, img_array):
        if model_name == "model1.h5":
            img_array = self.to_white_black_radical(img_array)
        else:
            img_array = self.to_white_black(img_array)
        img_array = self.crop(img_array)
        img_array = self.add_padding(img_array)
        img_array = self.resize(img_array)
        return img_array

    # crop image only to non-empty data
    def crop(self, img_array):
        coords = img_array == 0.
        drop_cols = np.all(coords, axis=0)
        drop_rows = np.all(coords, axis=1)

        first_col = drop_cols.argmin()
        first_row = drop_rows.argmin()
        last_col = len(drop_cols) - drop_cols[::-1].argmin()
        last_row = len(drop_rows) - drop_rows[::-1].argmin()

        return img_array[first_row:last_row, first_col:last_col]

    def resize(self, img_array):
        return cv2.resize(img_array, dsize=(28, 28))

    def to_white_black_radical(self, img_array):
        mins_ = np.min(img_array, axis=-1)
        mins_ = np.where(mins_ == 255, 0., 1.)
        mins_ = mins_.astype(np.float32)
        return mins_

    def to_white_black(self, img_array):
        grayValue = 0.07 * img_array[:,:,2] + 0.72 * img_array[:,:,1] + 0.21 * img_array[:,:,0]
        gray_img = grayValue.astype(np.float32)
        return gray_img

    def decode_label(self, one_hots):
        return np.argmax(one_hots)

    def add_padding(self, img_array):
        return np.pad(img_array, self.padding)

    def save(self, img_array):
        path = os.path.join("samples", f"sample_{self.id_}.npy")
        self.id_ += 1
        np.save(path, img_array)


os.makedirs("samples", exist_ok=True)
predictor = Predictor()