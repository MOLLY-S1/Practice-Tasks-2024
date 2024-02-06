fish_list = ["flounder", "sole", "blue cod", "snapper", "terakihi",
             "john dory", "red cod"]
new_list = []
for fish in fish_list:
    letters = list(fish)
    new_list.append(letters)

for i in new_list:
    print([i][0][0])

print(new_list[0][0])
print(new_list[0][1])
print(new_list[0][2])

fish_len = []
for fish in fish_list:
    length = len(fish)
    fish_len.append(length)
    biggest = fish_len.index(max(fish_len))

print(fish_list[biggest])

spaces =[]
for i in new_list:
        if " " in i:
                spaces.append(new_list.index(i))

for i in spaces:
        print(fish_list[i])

print("----------------------------------------")

cods =[]
for name in fish_list:
        if "cod" in name:
                cods.append(fish_list.index(name))

for name in cods:
        print(fish_list[name])
