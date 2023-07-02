class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        sum_of_asccii = 0
        for ch in str(key):
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable, handling collisions as needed.
        If the given key already exists, replaces its value with the new value.

        Args:
            key: The key to set in the hashtable.
            value: The corresponding value for the key.

        Returns:
            None
        """
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hashtable.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key, or None if the key doesn't exist.
        """
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.

        Args:
            key: The key to check for existence.

        Returns:
            bool: True if the key exists in the hashtable, False otherwise.
        """
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return True
        return False

    def keys(self):
        """
        Returns a collection of all unique keys in the hashtable.

        Returns:
            list: A list of all unique keys in the hashtable.
        """
        keys = []
        for bucket in self.table:
            for kvp in bucket:
                keys.append(kvp[0])
        return list(set(keys))

   



    
if __name__ == "__main__":
    ht = Hashtable()
    ht.set('a', 1)
    ht.set('b', 2)
    ht.set('c', 3)
    ht.set('d', 4)
    ht.set('e', 5)
    ht.set('f', 6)
    ht.set('g', 7)
    ht.set('h', 8)
    ht.set('i', 9)
    ht.set('j', 10)
    ht.set('k', 11)
    ht.set('l', 12)
    ht.set('m', 13)
    ht.set('n', 14)
    ht.set('o', 15)
    ht.set('p', 16)
    ht.set('q', 17)
    ht.set('r', 18)
    ht.set('s', 19)
    ht.set('t', 20)
    ht.set('u', 21)
    ht.set('v', 22)
    ht.set('w', 23)
    ht.set('x', 24)
    ht.set('y', 25)
    ht.set('z', 26)
    print(ht.get('a'))
    print(ht.get('b'))
    print(ht.get('c'))
    print(ht.get('d'))
    print(ht.get('e'))
    print(ht.get('f'))
    print(ht.get('g'))
    print(ht.get('h'))
    print(ht.get('i'))
    print(ht.get('j'))
    print(ht.get('k'))
    print(ht.get('l'))
    print(ht.get('m'))
    print(ht.get('n'))
    print(ht.get('o'))
    print(ht.get('p'))
    print(ht.get('q'))
    
    