import numpy as np
import os
import argparse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.utils import to_categorical


def load_data(data_file_name, data_dir='./data'):
    X_train, X_test, y_train, y_test = np.load(
        os.path.join(
            *[data_dir, '{file_name}.npy'.format(file_name=data_file_name)]),
        allow_pickle=True
    )

    return X_train, X_test, y_train, y_test

def create_model(image_size, num_classes):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu',
                     input_shape=(image_size, image_size, 3)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    # opt = SGD(lr=0.01)
    opt = Adam()
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt, metrics=['accuracy'])

    return model


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file_name')
    parser.add_argument('image_size')
    args = parser.parse_args()

    X_train, X_test, y_train, y_test = load_data(
        data_file_name=args.data_file_name
    )

    classes = list(set(y_train) | set(y_test))
    num_classes = len(classes)
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    model = create_model(
        image_size=args.image_size,
        num_classes=num_classes
    )

    model.fit(X_train, y_train, batch_size=32, epochs=20)

    score = model.evaluate(X_test, y_test, batch_size=32)
