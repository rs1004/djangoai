import numpy as np
import argparse
import os
from tensorflow.keras.models import load_model
from PIL import Image

def load_image(file_path, image_size):
    image = Image.open(file_path).convert('RGB').resize((image_size, image_size))
    data = np.asarray(image)

    return data

def predict(data, model):
    classes = os.listdir('./data')
    result = model.predict([[data]])[0]
    predicted = result.argmax()
    print('predict: {cls} with score: {score}'.format(cls=classes[predicted], score=result[predicted] * 100))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_size', type=int)
    parser.add_argument('image_path')
    parser.add_argument('model_path')
    args = parser.parse_args()

    data = load_image(
        file_path=args.image_path,
        image_size=args.image_size
    )

    model = load_model(args.model_path)

    predict(
        data=data,
        model=model
    )
