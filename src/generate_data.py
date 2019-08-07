import os
import glob
import argparse
import numpy as np
from PIL import Image
from sklearn import model_selection


def generate_data(data_dir='./data', image_size=150):
    classes = os.listdir(data_dir)
    num_classes = len(classes)

    X = []
    Y = []

    for index, class_label in enumerate(classes):
        files = glob.glob(os.path.join(*[data_dir, class_label, '*.jpg']))
        for file in files:
            image = Image.open(file)
            image = image.convert('RGB')
            image = image.resize((image_size, image_size))
            data = np.asarray(image) / 255.0
            X.append(data)
            Y.append(index)
    
    return X, Y


def save(save_dir, X, Y):
    X = np.array(X)
    Y = np.array(Y)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
    xy = (X_train, X_test, y_train, y_test)

    np.save(os.path.join(save_dir, 'imagefiles.npy'), xy)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('save_dir')
    args = parser.parse_args()

    X, Y = generate_data()
    save(
        save_dir=args.save_dir,
        X=X,
        Y=Y
    )
