from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
import pandas as pd
from os import path, mkdir
from string import Template
from shutil import copy
from keras.preprocessing.image import ImageDataGenerator

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