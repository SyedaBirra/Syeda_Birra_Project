import mmh3
import math
import bitarray
import random

class BloomFilter:
    def __init__(self, n, hash_count):
        # n is the number of items , hash_count is the no. of hash functions
        self.size=int((2*n)/math.log(2))  
        self.hash_count=hash_count
        self.bit_array=bitarray.bitarray(self.size)
        self.bit_array.setall(0)
        self.seeds=[random.randint(1,100)for _ in range(hash_count) ]  

    
    def hashes(self,item):
        #Generating multiple hash values
        pass
    
    #To add an item to BloomFilter
    def add(self, item):
        
        pass
    
    #To check an item in the Bloom filter
    def check(self, item):
        pass