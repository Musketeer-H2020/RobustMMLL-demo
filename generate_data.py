"""
@author:  Zaid
September 2020

Example of use: python generate_data.py

"""

import tensorflow as tf
from keras.utils.np_utils import to_categorical
import numpy as np
from math import floor

import pickle


def getMNISTdata(perc_users, labels, validation_split=None):
    perc_users = perc_users / np.sum(perc_users)
    nusers = np.shape(perc_users)[0]
    num_classes = 10

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    x_train = x_train.reshape((x_train.shape[0], -1))
    x_test = x_test.reshape((x_test.shape[0], -1))
    xtr = None
    ytr = None
    for e in labels:
        idx = (y_train == e)
        if xtr is None or ytr is None:
            xtr = x_train[idx, :]
            ytr = y_train[idx]
        else:
            xtr = np.concatenate((xtr, x_train[idx, :]), axis=0)
            ytr = np.concatenate((ytr, y_train[idx]), axis=0)

    ntr = np.shape(xtr)[0]
    r = np.random.permutation(np.shape(xtr)[0])
    xtr = xtr[r, :]
    ytr = ytr[r]

    if validation_split is not None:
        nval = floor(validation_split * ntr)
        xval = xtr[-nval:, :]
        yval = ytr[-nval:]
        xtr = xtr[:ntr - nval, :]
        ytr = ytr[:ntr - nval]
        ntr = np.shape(xtr)[0]

    yval = to_categorical(yval, num_classes=num_classes)
    ytr = to_categorical(ytr, num_classes=num_classes)
    ntr_users = np.floor(np.array(perc_users) * ntr)

    training_data = []
    training_labels = []
    it = 0
    for i in range(nusers):
        x = xtr[it:it + int(ntr_users[i]), :]
        y = ytr[it:it + int(ntr_users[i]), :]
        training_data.append(x)
        training_labels.append(y)
        it = it + int(ntr_users[i])

    xtst = None
    ytst = None
    for e in labels:
        idx = (y_test == e)
        if xtst is None or ytst is None:
            xtst = x_test[idx, :]
            ytst = y_test[idx]
        else:
            xtst = np.concatenate((xtst, x_test[idx, :]), axis=0)
            ytst = np.concatenate((ytst, y_test[idx]), axis=0)

    ytst = to_categorical(ytst, num_classes=num_classes)

    return training_data, training_labels, xval, yval, xtst, ytst


if __name__ == "__main__":
    dataset_name = 'mnist'
    file = 'input_data/' + dataset_name + '_hackathon_data.pkl'
    # Proportion of data for each worker, length of list corresponds to data partitions or worker partitions
    perc_users = [0.1, 0.15, 0.2, 0.2, 0.1, 0.15, 0.1]
    labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    perc_users = [0.2, 0.2, 0.2, 0.2, 0.2]
    labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Currently all labels are used in data partitions, but only a subset of labels can be chosen here e.g., [0, 2, 5, 7]

    data_hackathon = getMNISTdata(perc_users, labels, validation_split=0.1)
    with open(file, "wb") as f:
        pickle.dump(data_hackathon, f)
