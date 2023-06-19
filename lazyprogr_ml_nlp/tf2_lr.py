import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow import keras

from keras.layers import Dense, Input
from keras.models import Model
from keras.optimizers import Adam

N = 100
X = np.random.random(N) * 6 -3
y = 0.5 * X - 1 + np.random.randn(N) * 0.5

print(tf.__version__)

plt.scatter(X, y)

# build model
i = Input(shape=(1,))
x = Dense(1)(i)

model = Model(i, x)

print("test")