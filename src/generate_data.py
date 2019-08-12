import os
import glob
import argparse
import numpy as np
from PIL import Image
from sklearn import model_selection


def generate_data(image_size, data_dir='./data'):
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
            data = np.asarray(image)
            X.append(data)
            Y.append(index)
    
    return X, Y


def save(X, Y, save_file_name, save_dir='./data'):
    X = np.array(X)
    Y = np.array(Y)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
    xy = (X_train, X_test, y_train, y_test)

    np.save(os.path.join(save_dir, '{file_name}.npy'.format(file_name=save_file_name)), xy)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_size', type=int)
    parser.add_argument('save_file_name')
    args = parser.parse_args()

    X, Y = generate_data(
        image_size=args.image_size
    )
    save(
        X=X,
        Y=Y,
        save_file_name=args.save_file_name
    )
