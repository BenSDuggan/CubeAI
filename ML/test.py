import tensorflow as tf
import random
import numpy as np
from Cube import *


def ml():
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=3)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss)
    print(val_acc)

def move_key(n=2):
    max_move = Cube(n).moves
    global num_to_moves
    num_to_moves = []
    for i in range(max_move+1):
        for j in range(1,4):
            num_to_moves.append((i,j))
    num_to_moves.append((-1,-1))

    global moves_to_num
    moves_to_num = {}
    for i in range(len(num_to_moves)):
        moves_to_num[num_to_moves[i]] = i

def generate_data(length, n=2):
    global moves_to_num

    X_train = []
    y_train = []
    c = Cube(n)
    count = 0

    while count < length:
        num = random.randint(0,c.moves)
        if num == c.moves+1:
            c = Cube(n)
            continue
        degree = random.randint(1,3)
        c.makeMove((num,degree))
        X_train.append(c.state)
        if c.isSolved():
            y_train.append(moves_to_num[(-1,-1)])
        elif degree == 1:
            y_train.append(moves_to_num[(num,3)])
        elif degree == 2:
            y_train.append(moves_to_num[(num,2)])
        elif degree == 3:
            y_train.append(moves_to_num[(num,1)])
        count += 1

    return np.array(X_train), np.array(y_train)


if __name__ == '__main__':
    move_key(2)
    global num_to_moves
    global moves_to_num

    X_train, y_train = generate_data(10000000,2)
    X_train = tf.keras.utils.normalize(X_train, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(len(num_to_moves),activation=tf.nn.softmax))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=3)

    X_test, y_test = generate_data(1000,2)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    val_loss, val_acc = model.evaluate(X_test, y_test)
    print(val_loss)
    print(val_acc)
