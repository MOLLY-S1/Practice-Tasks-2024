sentence = input("Enter string: ")
sentence = list(sentence)

letter = input("Enter letter to find: ")

counter = 0

new_list = []
for word in sentence:
    letters = list(word)
    new_list.append(letters)
for i in new_list:
    if letter in i:
       counter += 1

print(f"There are {counter} {letter}s in this sentence")
