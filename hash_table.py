class HashTable(object):
    def __setitem__(self, key, value):
        """ define dict-like insertion grammer """
        return self.add(key, value)

    def __getitem__(self, key):
        """ define dict-like query grammer """
        return self.get(key)

    def __str__(self):
        """ string to to printed when called by print() """
        HT_str = ''
        for i in range(len(self.array)):
            HT_str += 'bucket ' + str(i) + ': '
            if self.array[i] is not None:
                for kvp in self.array[i]:
                    HT_str += str(kvp) + ' '
            HT_str += '\n'

        return HT_str


    def __init__(self, length=16):
        """ Initialize empty hash table """
        self.array = [None] * length

        """ total number of elements in the Hash Table """
        self.count = 0


    def hash_function(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash_function(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
                self.count += 1
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            self.count += 1
    
    def get(self, key):
        """Get a value by key"""
        index = self.hash_function(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()

    def rehash(self, new_length=-1):
        # default to double the current size
        if new_length == -1:
            new_length = self.count *2

        new_HT = HashTable(length = new_length)

        for bucket in self.array:
            if bucket is not None:
                for kvp in bucket:
                    new_HT[kvp[0]] = kvp[1]

        self.count = new_HT.count
        self.array = new_HT.array