import numpy as np
import tensorflow as tf
import zipfile
import os
from keras.preprocessing import image
from tensorflow.keras import models
from tensorflow.python import keras
from path import sample_path
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

base_dir = sample_path+'/images'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')

# membuat direktori ruangan rapi pada direktori data training
train_clean_dir = os.path.join(train_dir, 'clean')

# membuat direktori ruangan berantakan pada direktori data training
train_messy_dir = os.path.join(train_dir, 'messy')

# membuat direktory ruangan rapi pada direktori data validasi
validtion_clean_dir = os.path.join(validation_dir, 'clean')

# membuat direktori ruangan berantakan pada dirktori data validasi
validation_messy_dir = os.path.join(validation_dir, 'messy')


# Recreate the exact same model, including its weights and the optimizer
new_model = load_model(sample_path+'/15.ts_first_model')

# Show the model architecture
new_model.summary()

# train image untuk dapat diberikan label 
# train_datagen = ImageDataGenerator(
#   rescale=1./255,
#   rotation_range=20,
#   horizontal_flip=True,
#   shear_range=0.2,
#   fill_mode='nearest',
# )

# # we prepare object image to train
# train_generator = train_datagen.flow_from_directory(
#   train_dir,
#   target_size=(150,150), # mengubah resolusi image menjadi 150x150px
#   batch_size=4, # batch size per sample
#   class_mode='binary', # karena kita merupakan kasifikasi 2 kelas maka menggunakan class_mode = 'binary'
# )


# #  check its accuracy
# loss, acc = new_model.evaluate(train_generator, verbose=2)
# print('Restored model, accuracy: {:5.2f}% and loss {:4.2f}'.format(100 * acc, loss))


# let's try with new image we got from google search
image_clean1 = image.load_img(sample_path+'/clean1.jpeg', target_size=(150, 150))
image_clean2 = image.load_img(sample_path+'/clean2.jpeg', target_size=(150, 150))
image_messy1 = image.load_img(sample_path+'/messy1.jpeg', target_size=(150, 150))
image_messy2 = image.load_img(sample_path+'/mess2.jpeg', target_size=(150, 150))
image_clean3 = image.load_img(sample_path+'/images/test/3.png', target_size=(150, 150))

x = image.img_to_array(image_clean3)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])

classes = new_model.predict(images, batch_size=20)
print(classes)

if classes==0:
  print('clean')
else:
  print('messy')
