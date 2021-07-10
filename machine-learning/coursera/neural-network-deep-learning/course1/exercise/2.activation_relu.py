import tensorflow as tf

# mnist dataset is a samples from integers to floating-point numbers;
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# NOTE, only user activation function "sigmoid" in output layer, other than that the hidden layer are useless.
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='sigmoid'),
  tf.keras.layers.Dense(10, activation='sigmoid')
])


predictions = model(x_train[:1]).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, steps_per_epoch=10,)

model.evaluate(x_test,  y_test, verbose=2)

# Without hidden layer
print("===========================================")
print("WITHOUT HIDDEN LAYER \n")
model2 = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(10, activation='sigmoid')
])


predictions = model2(x_train[:1]).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model2.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model2.fit(x_train, y_train, epochs=5, steps_per_epoch=10,)

model2.evaluate(x_test,  y_test, verbose=2)
