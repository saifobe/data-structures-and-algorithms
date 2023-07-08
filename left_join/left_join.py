from hash_table.hash_table import Hashtable

def left_join(hashmap1:Hashtable,hashmap2:Hashtable):

    arr = []

    for key in hashmap1.keys():
        hash1_val = hashmap1.get(key)

        if hashmap2.has(key):
            arr.append([key, hash1_val,hashmap2.get(key)])
        else:
            arr.append([key, hash1_val,None])
    return arr