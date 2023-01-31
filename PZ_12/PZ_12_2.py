def str_to_lower(crs: str):
    for ch in crs:
        yield ch.lower()

user_str = input("BIG LETTERS: ")
print(''.join(str_to_lower(user_str)))
