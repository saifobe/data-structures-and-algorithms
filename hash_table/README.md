# Hash Table
## Code Challenge: Class 30

### Emplement a Hash Table

* Create a class called `HashTable` and `Node`
* `Node` class should have `key`, `value`, and `next` properties
* `HashTable` class should have `add`, `get`, `contains`, and `hash` methods
* `add` method should hash the key, and add the key and value pair to the table, handling collisions as needed
* `get` method should accept a key, and return the value from the table
* `contains` method should accept a key, and return a boolean indicating if the key exists in the table already
* `hash` method should accept a key, and return an index in the collection

### Approach & Efficiency
* `add` method should hash the key, and add the key and value pair to the table, handling collisions as needed
  * Time: O(1)
  * Space: O(1)

[hash_table.py](hash_table.py)