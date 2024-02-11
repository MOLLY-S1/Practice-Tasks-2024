import easygui

breads = {"Wholemeal": 1,
          "White": 0.8,
          "Cheesy White": 1.2,
          "Gluten Free": 1.4}

meats = {"Chicken": 2.69,
         "Beef": 3,
         "Salami": 4,
         "Vegan Slice": 3.3}

garnishes = {"Onion": 1.69,
             "Tomato": 1,
             "Lettuce": 2,
             "Cheese": 2.5}

sandwich = {}


def bread():
    bread_choice = easygui.buttonbox("Please Choose your Bread:\n"
                                     "Wholemeal: $1\n"
                                     "White: $0.8\n"
                                     "Cheesy White: $1.2\n"
                                     "Gluten Free: $1.4\n",
                                     "BREAD",
                                     choices=["Wholemeal", "White",
                                              "Cheesy White", "Gluten Free"])

    sandwich[bread_choice] = breads[bread_choice]
    return bread_choice


def meat():
    meat_choice = easygui.buttonbox("Please Choose your meat:\n"
                                    "Chicken: $2.69\n" "Beef: $3\n"
                                    "Salami: $4\n" "Vegan Slice: $3.3\n",
                                    "MEAT",
                                    choices=["Chicken", "Beef",
                                             "Salami", "Vegan Slice"])
    sandwich[meat_choice] = meats[meat_choice]
    return meat_choice


def garnish():
    garnish_choice = easygui.buttonbox("Please Choose your garnish:\n"
                                       "Onion: $1.69\n"
                                       "Tomato: $1\n"
                                       "Lettuce: $2\n"
                                       "Cheese: $2.5\n",
                                       "GARNISH",
                                       choices=["Onion",
                                                "Tomato",
                                                "Lettuce",
                                                "Cheese"])
    sandwich[garnish_choice] = garnishes[garnish_choice]
    return garnish_choice


def confirm(bread_chosen, meat_chosen, garnish_chosen):
    while True:
        correct = easygui.buttonbox(f"Is the following sandwich correct?\n"
                                    f"--------------------------------\n"
                                    f"Bread: {bread_chosen} - $"
                                    f"{sandwich[bread_chosen]}\n"
                                    f"Meat: {meat_chosen} - $"
                                    f"{sandwich[meat_chosen]}\n"
                                    f"Garnish: {garnish_chosen} - $"
                                    f"{sandwich[garnish_chosen]}\n"
                                    f"Total - $"
                                    f"{sandwich[garnish_chosen] + sandwich[meat_chosen] + sandwich[bread_chosen]:.2}",
                                    "CONFIRM",
                                    choices=["Yes", "No"])

        if correct == "Yes":
            easygui.msgbox("Thanks for ordering!", "GOODBYE")
            break

        change = easygui.buttonbox(f"What would you like to change:\n",
                                   "CHANGE "
                                   "SANDWICH",
                                   choices=["Bread", "Meat", "Garnish"])
        if change == "Bread":
            sandwich.pop(bread_chosen)
            bread_chosen = easygui.buttonbox("Please Choose your Bread:\n"
                                             "Wholemeal: $1\n"
                                             "White: $0.8\n"
                                             "Cheesy White: $1.2\n"
                                             "Gluten Free: $1.4\n",
                                             "BREAD",
                                             choices=["Wholemeal", "White",
                                                      "Cheesy White",
                                                      "Gluten Free"])
            sandwich[bread_chosen] = breads[bread_chosen]


        if change == "Meat":
            sandwich.pop(meat_chosen)
            meat_chosen = easygui.buttonbox("Please Choose your meat:\n"
                                            "Chicken: $2.69\n" "Beef: $3\n"
                                            "Salami: $4\n" "Vegan Slice: $3.3\n",
                                            "MEAT",
                                            choices=["Chicken", "Beef",
                                                     "Salami", "Vegan Slice"])
            sandwich[meat_chosen] = meats[meat_chosen]


        if change == "Garnish":
            sandwich.pop(garnish_chosen)
            garnish_chosen = easygui.buttonbox("Please Choose your garnish:\n"
                                               "Onion: $1.69\n"
                                               "Tomato: $1\n"
                                               "Lettuce: $2\n"
                                               "Cheese: $2.5\n",
                                               "GARNISH",
                                               choices=["Onion",
                                                        "Tomato",
                                                        "Lettuce",
                                                        "Cheese"])
            sandwich[garnish_chosen] = garnishes[garnish_chosen]


# # MAIN ROUTINE
b = bread()
m = meat()
g = garnish()
confirm(b, m, g)
