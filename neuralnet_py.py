from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np


#X = np.load("C:/Users/amman/Downloads/GSU/Senior/Spring 2019/Deep Learning/DL_Project/X_data.npy")
#y = pickle.load(open("C:/Users/amman/Downloads/GSU/Senior/Spring 2019/Deep Learning/DL_Project/y.pickle", "rb"))

#X = X/255.0
#y = np.array(y)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss="categorical_crossentropy",
             optimizer="adam",
             metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'img_data/training_data',
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical')

testing_set = test_datagen.flow_from_directory(
        'img_data/testing_data',
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical')

model.fit_generator(
        training_set,
        steps_per_epoch=900,
        epochs=2,
        validation_data=testing_set,
        validation_steps=100)
