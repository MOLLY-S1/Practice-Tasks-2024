sentence = input("Enter string: ")
sentence = list(sentence)
counter = 0

new_list = []
for word in sentence:
    letters = list(word)
    new_list.append(letters)
for i in new_list:
    if "e" in i:
       counter += 1

print(f"There are {counter} es in this sentence")
