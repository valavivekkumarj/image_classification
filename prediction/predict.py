import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class dogCat:
    def __init__(self, filename):
        self.filename = filename

    def predictionDogCat(self):
        model = load_model(os.path.join("model", "model.h5"))

        image_name = self.filename

        test_image = image.load_img(image_name, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] != 1:
            prediction = "Cat"
            return [{"img": prediction}]
        else:
            prediction = "DOG"
            return [{"img": prediction}]
