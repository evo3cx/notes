import numpy as np
import tensorflow as tf
import zipfile
import os
from tensorflow.keras.preprocessing import image
from path import sample_path
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# melakukan ekstraksi pada file zip
# local_zip = sample_path+'/messy-and-clean-image.zip'
# zip_ref = zipfile.ZipFile(local_zip, 'r')
# zip_ref.extractall()
# zip_ref.close()
 
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

# train image untuk dapat diberikan label 
train_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=20,
  horizontal_flip=True,
  shear_range=0.2,
  fill_mode='nearest',
)

test_datagen = ImageDataGenerator(
  rescale=1./255,
  rotation_range=20,
  horizontal_flip=True,
  shear_range=0.2,
  fill_mode='nearest',
)

# we prepare object image to train
train_generator = train_datagen.flow_from_directory(
  train_dir,
  target_size=(150,150), # mengubah resolusi image menjadi 150x150px
  batch_size=4, # batch size per sample
  class_mode='binary', # karena kita merupakan kasifikasi 2 kelas maka menggunakan class_mode = 'binary'
)

validation_generator = test_datagen.flow_from_directory(
  validation_dir, # direktori data validasi
  target_size=(150, 150),
  batch_size=4,
  class_mode='binary'
)


# create the model, we use Convolution Layer to extract every data from image
# then reduce it with max pooling without remove the information
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
  tf.keras.layers.MaxPool2D(2, 2),
  tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
  tf.keras.layers.MaxPool2D(2, 2),
  tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
  tf.keras.layers.MaxPool2D(2, 2),
  tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
  tf.keras.layers.MaxPool2D(2, 2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])


# compile model dengan 'adam' optimizer loss function 'binary_crossentropy' 
model.compile(loss='binary_crossentropy',
              optimizer=tf.optimizers.Adam(),
              metrics=['accuracy'])


# latih model dengan model.fit 
model.fit(
      train_generator,
      steps_per_epoch=25,  # berapa batch yang akan dieksekusi pada setiap epoch
      epochs=20, # tambahkan eposchs jika akurasi model belum optimal
      validation_data=validation_generator, # menampilkan akurasi pengujian data validasi
      validation_steps=5,  # berapa batch yang akan dieksekusi pada setiap epoch
      verbose=2)


# view model summary
model.summary()

# save my model, so we can use it later
model.save(sample_path+'/15.ts_first_model')


# let's try with new image we got from google search
image_clean1 = image.load_img(sample_path+'/clean1.jpeg', target_size=(150, 150))
image_clean2 = image.load_img(sample_path+'/clean2.jpeg', target_size=(150, 150))
image_messy1 = image.load_img(sample_path+'/messy1.jpeg', target_size=(150, 150))
image_messy2 = image.load_img(sample_path+'/mess2.jpeg', target_size=(150, 150))
image_clean3 = image.load_img(sample_path+'/images/test/3.png', target_size=(150, 150))

x = image.img_to_array(image_clean3)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])


classes = model.predict(images, batch_size=20)
print(classes)

if classes==0:
  print('clean')
else:
  print('messy')
