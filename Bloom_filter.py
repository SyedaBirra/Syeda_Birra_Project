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
        return [(hash(item)+seed)%self.size for seed in self.seeds]
    
    #To add an item to BloomFilter
    def add(self, item):
        
        for index in self.hashes(item):
            self.bit_array[index]=True
    
    #To check an item in the Bloom filter
    def check(self, item):
        return all(self.bit_array[index] for index in self.hashes(item))
    
    
    
# EXAMPLE USAGE

if __name__ == "__main__":
    n_items=100  # Expected number of items
    hash_count=3  # Number of hash functions
    
    # Initialize Bloom filter
    bloom_filter=BloomFilter(n=n_items, hash_count=hash_count)
    
    # Adding items
    items_adding=["Syeda","Birra","Zainab","Sherazi","Alex"]
    for item in items_adding:
        bloom_filter.add(item)
    # Checking itemss
    items_checking=["Syeda","Birra","Zainab","Sherazi","Alex","Becky"]
    for item in items_checking:
        result=bloom_filter.check(item)
        print(f"{item} is {'possibly in bloom filter'if result else 'definitely not in bloom filter'}")

#Testing







