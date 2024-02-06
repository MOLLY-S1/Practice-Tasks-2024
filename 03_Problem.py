sentence = input("Enter string: ")
sentence = list(sentence)
print(sentence)
new_list = []
for word in sentence:
    letters = list(word)
    new_list.append(letters)


es =[]
for i in new_list:
        if "e" in i:
                es.append(new_list.index(i))

for i in es:
        print(sentence[i])
