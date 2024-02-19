import sys

def string_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list

abc = list('abcdefghijklmnopqrstuvwxyz')
words = [
    "apple", "banana", "cat", "dog", "elephant", "fish",
    "grape", "house", "igloo", "jungle", "kangaroo", "lemon",
    "monkey", "nest", "orange", "pear", "quilt", "rabbit",
    "snake", "tiger", "umbrella", "violet", "watermelon", "xylophone",
    "yoga", "zebra"]
for letter in abc:
    print(f"{letter} {letter.upper()}")

input_letter =string_to_ascii(sys.argv[1].lower())[0]
word_index = input_letter-97
print(words[word_index])

N = int(sys.argv[2])
table = []
for i in range(1,N+1):
    arr = []
    for j in range(1,N+1):
        arr.append(i*j)
    table.append(arr)

print(table)

num = int(sys.argv[3])
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
if isPrime:
    print(f"Number: {num} is prime")
else:
        print(f"Number: {num} isn't prime")