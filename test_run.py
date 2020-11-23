import numpy as np
from hash_table import *
from generate_data import create_json_file, decode_json_file

if __name__ == '__main__':
    # create json file of random integers
    create_json_file('integer_data.json')

    # read from json file, store data as ndarray
    data_array = np.array(decode_json_file('integer_data.json'))
    print("data to be inserted: ", data_array[0], '\n')

    # create empty Hash Table with 10 buckets
    HT = HashTable(length=10)


    # use second order hash
    HT.hash_function = HT.second_order_hash

    #insert data into Hash Table
    for j in range(len(data_array[0])):
        HT.add(data_array[0][j],-1)

    print("Hash Table before rehash: \n", HT)

    # rehash Hash Table, default to double table size
    HT.rehash()
    print("Hash Table after rehash: \n", HT)