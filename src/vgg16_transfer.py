import numpy as np
import os
import argparse
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import VGG16


def load_data(data_file_name, data_dir='./output'):
    X_train, X_test, y_train, y_test = np.load(
        os.path.join(
            *[data_dir, '{file_name}.npy'.format(file_name=data_file_name)]),
        allow_pickle=True
    )

    return X_train, X_test, y_train, y_test

def create_model(image_size):
    model = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))

    top_model = Sequential()
    top_model.add(Flatten(input_shape=model.output_shape[1:]))
    top_model.add(Dense(256, activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(num_classes, activation='softmax'))

    model = Model(inputs=model.input, outputs=top_model(model.output))

    for layer in model.layers[:15]:
        layer.trainable = False
    
    opt = Adam(lr=0.0001)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

    return model


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_size', type=int)
    parser.add_argument('data_file_name')
    args = parser.parse_args()

    X_train, X_test, y_train, y_test = load_data(
        data_file_name=args.data_file_name
    )

    X_train = X_train.astype(float) / 255.0
    X_test = X_test.astype(float) / 255.0

    classes = list(set(y_train) | set(y_test))
    num_classes = len(classes)
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    model = create_model(
        image_size=args.image_size
    )

    model.fit(X_train, y_train, batch_size=32, epochs=17)
    score = model.evaluate(X_test, y_test, batch_size=32)

    model.save('./model/vgg16_transfer.h5')
