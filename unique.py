def is_unique(string):
    lowercase = string.lower()
    characters = set()

    for char in lowercase:
        if char == ' ':
            continue
        if char in characters:
            return False
        characters.add(char)

    return True


if __name__ == '__main__':
    print(is_unique('abcde'))
    print(is_unique('abcdea'))
    print(is_unique('abcdea '))
    print(is_unique('abcdea  '))
