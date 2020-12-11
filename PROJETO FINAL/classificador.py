from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
import pandas as pd
from os import path, mkdir
from string import Template
from shutil import copy
from keras.preprocessing.image import ImageDataGenerator

all_data = pd.read_csv('all.csv')

classificador = Sequential()

classificador.add(Conv2D(64, (3,3), input_shape = (64,64,3), activation = 'relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D())

classificador.add(Conv2D(64, (3,3), input_shape = (64,64,3), activation = 'relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D())

classificador.add(Flatten())

classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))

classificador.add(Dense(units = 6, activation = 'softmax'))

classificador.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics = ['accuracy'])

gerador_treinamento = ImageDataGenerator(rescale = 1./255, rotation_range = 7, horizontal_flip = True, shear_range = 0.2, height_shift_range = 0.07, zoom_range = 0.2)
gerador_teste = ImageDataGenerator(rescale = 1.255)

base_treinamento = gerador_treinamento.flow_from_directory('data/training', target_size = (64,64), batch_size = 32, class_mode = 'categorical')
base_teste = gerador_teste.flow_from_directory('data/test', target_size = (64,64), batch_size = 32, class_mode = 'categorical')


classificador.fit_generator(base_treinamento, steps_per_epoch = 4000 /32, epochs = 200, validation_data = base_teste, validation_steps = 1000/32)














