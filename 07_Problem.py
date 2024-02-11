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

price_add = 0

bread_choice = easygui.buttonbox("Please Choose your Bread:\n"
                                 "Wholemeal: $1\n"
                                 "White: $0.8\n"
                                 "Cheesy White: $1.2\n"
                                 "Gluten Free: $1.4\n",
                                 "BREAD",
                                 choices=["Wholemeal", "White",
                                          "Cheesy White", "Gluten Free"])
price_add += breads[bread_choice]

meat_choice = easygui.buttonbox("Please Choose your meat:\n"
                                "Chicken: $2.69\n" "Beef: $3\n"
                                "Salami: $4\n" "Vegan Slice: $3.3\n",
                                "MEAT",
                                choices=["Chicken", "Beef",
                                         "Salami", "Vegan Slice"])
price_add += meats[meat_choice]

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

price_add += garnishes[garnish_choice]

confirm = easygui.buttonbox(f"Is the following combo correct?\n"
                            f"--------------------------------\n"
                            f"Bread: {bread_choice} - ${breads[bread_choice]}\n"
                            f"Meat: {meat_choice} - ${meats[meat_choice]}\n"
                            f"Garnish: {garnish_choice} - "
                            f"${garnishes[garnish_choice]}\n"
                            f"Total: ${price_add:.2f}", "CONFIRM", choices=["Yes",
                                                                        "No"])

if confirm == "Yes":
    easygui.msgbox("Thanks for ordering!", "GOODBYE")

while confirm == "No":
    change = easygui.buttonbox(f"What would you like to change:\n", "CHANGE "
                                                                    "SANDWICH",
                               choices=["Bread", "Meat", "Garnish"])
    if change == "Bread":
        price_add -= breads[bread_choice]
        bread_choice = easygui.buttonbox("Please Choose your Bread:\n"
                                         "Wholemeal: $1\n"
                                         "White: $0.8\n"
                                         "Cheesy White: $1.2\n"
                                         "Gluten Free: $1.4\n",
                                         "BREAD",
                                         choices=["Wholemeal", "White",
                                                  "Cheesy White",
                                                  "Gluten Free"])
        price_add += breads[bread_choice]
        confirm = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"--------------------------------\n"
                                    f"Bread: {bread_choice} - ${breads[bread_choice]}\n"
                                    f"Meat: {meat_choice} - ${meats[meat_choice]}\n"
                                    f"Garnish: {garnish_choice} - "
                                    f"${garnishes[garnish_choice]}\n"
                                    f"Total: ${price_add:.2f}", "CONFIRM",
                                    choices=["Yes",
                                             "No"])

    if change == "Meat":
        price_add -= meats[meat_choice]
        meat_choice = easygui.buttonbox("Please Choose your meat:\n"
                                        "Chicken: $2.69\n" "Beef: $3\n"
                                        "Salami: $4\n" "Vegan Slice: $3.3\n",
                                        "MEAT",
                                        choices=["Chicken", "Beef",
                                                 "Salami", "Vegan Slice"])
        price_add += meats[meat_choice]
        confirm = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"--------------------------------\n"
                                    f"Bread: {bread_choice} - ${breads[bread_choice]}\n"
                                    f"Meat: {meat_choice} - ${meats[meat_choice]}\n"
                                    f"Garnish: {garnish_choice} - "
                                    f"${garnishes[garnish_choice]}\n"
                                    f"Total: ${price_add:.2f}", "CONFIRM",
                                    choices=["Yes",
                                             "No"])

    if change == "Garnish":
        price_add -= garnishes[garnish_choice]
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

        price_add += garnishes[garnish_choice]
        confirm = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"--------------------------------\n"
                                    f"Bread: {bread_choice} - ${breads[bread_choice]}\n"
                                    f"Meat: {meat_choice} - ${meats[meat_choice]}\n"
                                    f"Garnish: {garnish_choice} - "
                                    f"${garnishes[garnish_choice]}\n"
                                    f"Total: ${price_add:.2f}", "CONFIRM",
                                    choices=["Yes",
                                             "No"])

if confirm == "Yes":
    easygui.msgbox("Thanks for ordering!", "GOODBYE")

#MAIN ROUTINE

price_add = 0
