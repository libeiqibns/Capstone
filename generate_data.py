import numpy as np
import matplotlib.pyplot as plt
import codecs, json

DATA_SIZE = 10
SAMPLE_SIZE = 10

def generate_int(data_size):
    randomNums = np.random.normal(scale=3, size=data_size)
    randomInts = np.round(randomNums)

    return randomInts


def create_json_file(filename):
    randomInts = generate_int(DATA_SIZE)
    data_array = randomInts

    for i in range (1, SAMPLE_SIZE):
        randomInts = generate_int(DATA_SIZE)
        data_array = np.vstack((data_array, randomInts))
    
    with open(filename, 'w') as integer_data:
        json.dump(data_array.tolist(),integer_data)


def decode_json_file(filename):
    with codecs.open(filename, 'r') as integer_data:
        data = integer_data.read()
        #print(data)
        json_data = json.loads(data)
        return json_data

    return None


if __name__ == '__main__':
    create_json_file('integer_data.json')
    #json_data = decode_json_file('integer_data.json')
    #print(json_data)
