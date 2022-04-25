import numpy as np
import os

data_path = f'bbh{os.sep}'
test_path = data_path + f'testing{os.sep}'
training_path = data_path + f'testing{os.sep}'


def load_data(path: str):
    dictionary = {str: [[[float]]]}
    labels = []

    for file_name_ext in os.listdir(path):
        if 'label' in file_name_ext.lower():
            labels = np.load(path + file_name_ext)
            continue

        file_name = file_name_ext[:-4]

        dictionary[file_name] = np.load(path + file_name_ext)

    return dictionary, labels


if __name__ == '__main__':
    test_data, test_labels = load_data(test_path)
    training_data, training_labels = load_data(training_path)

    data_length = len(test_data['testAccelerometer'])





