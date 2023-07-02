from hash_table.hash_table import Hashtable

def  repeated_word(str):
    """
    Takes in a string and returns the first repeated word in the string.

    Returns:
        str: The first repeated word in the string. 
    """
    words = str.replace(",","").replace(".","").split(" ")
    obj = Hashtable()
    for word in words:
        if obj.has(word.lower()):
            return word.lower()
        else:
            obj.set(word.lower(), word.lower()) 

if __name__ == "__main__":
    print(repeated_word("Once upon a time, there was a brave princess who..."))
    print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."))
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted me, and I didn’t realize I was dead yet..."))
        
