import easygui

breads = {"Wholemeal": 1,
          "White": 0.8,
          "Cheesy White": 1.2,
          "Gluten Free": 1.4}

meats = {"Chicken": 2.69,
         "Beef": 3,
         "Salami": 4,
         "Vegan Slice": 3.3}

garnishs = {"Onion": 1.69,
            "Tomato": 1,
            "Lettuce": 2,
            "Cheese": 2.5}


def garnish():
    garnish_choice = easygui.choicebox("Please Choose your garnish:",
                                       "Garnish",
                                       choices=["Onion: 1.69",
                                                "Tomato: 1",
                                                "Lettuce: 2",
                                                "Cheese: 2.5"])

    return garnish_choice


def meat():
    meat_choice = easygui.choicebox("Please Choose your meat:", "Meat",
                                    choices=["Chicken: 2.69", "Beef: 3",
                                             "Salami: 4", "Vegan Slice: 3.3"])

    return meat_choice


def bread():
    bread_choice = easygui.choicebox("Please Choose your bread:", "Bread",
                                     choices=["Wholemeal: 1",
                                              "White: 0.8",
                                              "Cheesy White: 1.2",
                                              "Gluten Free: 1.4"])
    return bread_choice


# main routine
bread()
meat()
garnish()
print(f"your order is {bread()} with {meat()} and {garnish()}")
