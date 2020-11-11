import numpy as np
import matplotlib.pyplot as plt
import json

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
    
    with open(filename, 'w') as data_file:
        json.dump(data_array.tolist(),data_file)


def decode_json_file(filename):
    with open(filename, 'r') as data_file:
        data = data_file.read()
        #print(data)
        json_data = json.loads(data)
        return json_data

    return None


if __name__ == '__main__':
    create_json_file('integer_data.json')
    #json_data = decode_json_file('integer_data.json')
    #print(json_data)
