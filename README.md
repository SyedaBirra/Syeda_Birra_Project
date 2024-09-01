# **Syeda_Birra_Project**

### Project of Concept of Data Science : Bloom Filter
---

**Overview:**
This is a Python implementation of a simple Bloom filter, a data structure used to check if an item is part of a set. Bloom filters are probabilistic, meaning they may produce false positives but never false negatives.

---

**Contents:**
* Bloom_filter.py:
It contains 'BloomFilter' class with functions to add and check whether an item contains in the set. It also includes example and basic tests to verify that the Bloom Filter works as expected.
* README.md: This file contains the contents of the repository as well as a summary of the conclusions.
---

**Summary:**
This version of the Bloom filter is effective for rapid membership testing. When there is little memory and a little chance of false positives is acceptable, it performs well. The provided tests show that it handles both expected and unexpected input correctly.

**Installation:**
Make sure you have Python 3.11.4 installed. You'll also need following modules:

```python
pip install bitarray
pip install math
pip install random
```




