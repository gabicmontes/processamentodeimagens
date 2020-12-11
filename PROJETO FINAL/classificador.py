from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
import pandas as pd
from os import path, mkdir
from string import Template
from shutil import copy, move
from keras.preprocessing.image import ImageDataGenerator
import os
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint

all_data = pd.read_csv('all.csv')
all_data['GalaxyID'] = all_data['GalaxyID'].astype(str)

nomes_colunas = {
    'GalaxyID': 'GalaxyID',
    'Class7.1': 'completely_round',
    'Class7.2': 'in_between',
    'Class7.3': 'cigar_shaped',
    'Class2.1': 'on_edge',
    'Class4.1': 'has_signs_of_spiral',
    'Class3.1': 'spiral_barred',
    'Class3.2': 'spiral'
}

colunas = list(nomes_colunas.values())
training_df = all_data.rename(columns=nomes_colunas)[colunas]

has_sign_of_spiral = training_df['has_signs_of_spiral'] >= 0.75
completely_round_df = training_df[training_df['completely_round'] >= 0.65]
in_between_df = training_df[training_df['in_between'] >= 0.65]
cigar_shaped_df = training_df[training_df['cigar_shaped'] >= 0.65]
on_edge_df = training_df[training_df['on_edge'] >= 0.75]
spiral_barred_df = training_df[(training_df['spiral_barred'] >= 0.75) & has_sign_of_spiral]
spiral_df = training_df[(training_df['spiral'] >= 0.75) & has_sign_of_spiral]

if path.isdir('data/training') is False:
    mkdir('data/training')
    '''
for _, _, arquivo in os.walk('data/training/spiral'):
    pass

for i in range (1, len(arquivo) - 10, 10):
    move('data/training/spiral/'+arquivo[i], 'data/test/spiral/'+arquivo[i])
'''
def copy_images(df, dest):
    src_path = Template('data/images_training_rev1/$name.jpg')
    dest_path = Template('data/training/$folder/').substitute(folder=dest)

    if path.isdir(dest_path) is True:
        return

    mkdir(dest_path)
    for index, image in df.iterrows():
        copy(src_path.substitute(name=image['GalaxyID']), dest_path)

copy_images(completely_round_df, 'completely_round')
copy_images(in_between_df, 'in_between')
copy_images(cigar_shaped_df, 'cigar_shaped')
copy_images(on_edge_df, 'on_edge')
copy_images(spiral_barred_df, 'spiral_barred')
copy_images(spiral_df, 'spiral')



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


classificador.add(Dense(units = 6, activation = 'softmax'))

classificador.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics = ['acc'])



gerador_treinamento = ImageDataGenerator(rescale = 1./255, rotation_range = 7, horizontal_flip = True, shear_range = 0.2, height_shift_range = 0.07, zoom_range = 0.2)
gerador_teste = ImageDataGenerator(rescale = 1.255)
gerador_validacao = ImageDataGenerator(rescale = 1.255)

base_treinamento = gerador_treinamento.flow_from_directory('data/training', target_size = (64,64), batch_size = 32, class_mode = 'categorical')
base_teste = gerador_teste.flow_from_directory('data/test', target_size = (64,64), batch_size = 32, class_mode = 'categorical')
base_validacao = gerador_teste.flow_from_directory('data/validation', target_size = (64,64), batch_size = 32, class_mode = 'categorical')

model_checkpoint = ModelCheckpoint('weights/weights{epoch:08d}.h5', save_weights_only=True, period=5)

resultado_treinamento = classificador.fit_generator(base_treinamento, 
                            steps_per_epoch = 4000 /32, 
                            epochs = 50, 
                            validation_data = base_teste, 
                            validation_steps = 1000/32,
                            callbacks=[model_checkpoint])

classificador.save_weights('weights.h5')

history_dict = resultado_treinamento.history
print(history_dict.keys())

plt.subplot(2,2,1),plt.plot(resultado_treinamento.history['acc'])
plt.subplot(2,2,1),plt.plot(resultado_treinamento.history['val_acc'])
plt.subplot(2,2,1),plt.title('Model accuracy')
plt.subplot(2,2,1),plt.ylabel('Accuracy')
plt.subplot(2,2,1),plt.xlabel('Epoch')
plt.subplot(2,2,1),plt.legend(['Train', 'Test'], loc='upper left')


# Loss
plt.subplot(2,2,2),plt.plot(resultado_treinamento.history['loss'])
plt.subplot(2,2,2),plt.plot(resultado_treinamento.history['val_loss'])
plt.subplot(2,2,2),plt.title('Model loss')
plt.subplot(2,2,2),plt.ylabel('Loss')
plt.subplot(2,2,2),plt.xlabel('Epoch')
plt.subplot(2,2,2),plt.legend(['Train', 'Test'], loc='upper left')

plt.show()
