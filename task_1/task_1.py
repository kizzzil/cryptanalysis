import random

ALPHABET = "abcdefghigklmnopqrstuvwxyz0123456789"
MESSAGE = "McDonald's Corporation, doing business as McDonald's, is an American multinational fast food chain, founded in 1940 as a restaurant operated by Richard and Maurice McDonald, in San Bernardino, California, United States. They rechristened their business as a hamburger stand and later turned the company into a franchise, with the"

def filter_text(text, alphabet):
    return "".join([char for char in text.lower() if char in alphabet])
    
if __name__ == "__main__":
    # len_key = random.randint(2, len(ALPHABET))
    len_key = 3
    key = [x for x in range(len_key)]
    random.shuffle(key)

    text = filter_text(MESSAGE, ALPHABET)
    long_key = key * (len(text) // len_key) + key[:len(text) % len_key:] 
    long_key = [long_key[i] + len_key * (i // len_key) for i in range(len(long_key))]
    
    # print(len(long_key), " : ", len(text))
    encode_text = ["" for _ in range(len(text) + len_key)]
    # print(len(encode_text))
    for i in range(len(text)):
        encode_text[long_key[i]] = text[i]
    print(encode_text)
    
