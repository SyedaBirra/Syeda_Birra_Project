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


bloomfilter=BloomFilter(n=1000,hash_count=5)


words_to_insert=["horse","comb","snake","letter","book","flag", "egg", "bell","shop","shoe"]

# Insert words into the Bloom filter
for word in words_to_insert:
    bloomfilter.add(word)

unique_words=set(words_to_insert)

# Verify that all inserted words are found in the Bloom filter
for word in unique_words:
    assert bloomfilter.check(word),f'{word} not found in Bloom filter.'


words_not_inserted = ["nose","tree","bee","rarin","fire","bath","ice","vote", "car", "cat"]

# Check that words not inserted are not found in the Bloom filter
for word in words_not_inserted:
    if bloomfilter.check(word):
        print(f"False positive detected for {word}")
    else:
        print(f"{word} correctly identified as not present in Bloom filter.")

# Additional check: Ensure that all words in unique_words are  found
all_checked_words=[word for word in unique_words if bloomfilter.check(word)]
assert len(all_checked_words) == len(unique_words), \
       f'{len(all_checked_words)} words found, expected {len(unique_words)}'










