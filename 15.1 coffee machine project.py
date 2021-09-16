menu = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }
total_resources = {
        "water": 500,
        "milk": 500,
        "coffee": 500,
    }
money = 0
end = True

def espresso():
    """ask usr for coins and check if coins > price and then give coffee """

    price = int(menu["espresso"]["cost"])
    print(f"price of espresso is {price}")
    print("please enter coins!")
    usr_quarter = int(input("enter the amount of quarter:"))
    usr_dime = int(input("enter the amount of dime:"))
    usr_nickel = int(input("enter the amount of nickel:"))
    usr_penny = int(input("enter the amount of penny:"))

    usr_total_money = (usr_quarter/4) + (usr_dime/10) + (usr_nickel/20) + (usr_penny/100)
    price = int(menu["espresso"]["cost"])
    total_change = usr_total_money - price

    if usr_total_money < price:
        print(f"sorry! you are ${price - usr_total_money} short."
              f"here is your refund of ${usr_total_money}."
              f"try again with more coins.")
    else:
        print(f"you're espresso cost ${price} and here is the remaining change ${total_change}")
        print("enjoy you're espresso")
        # global money
        # money += price

def latte():
    """ask usr for coins and check if coins > price and then give latte """

    price = int(menu["latte"]["cost"])
    print(f"price of latte is {price}")
    print("please enter coins!")
    usr_quarter = int(input("enter the amount of quarter:"))
    usr_dime = int(input("enter the amount of dime:"))
    usr_nickel = int(input("enter the amount of nickel:"))
    usr_penny = int(input("enter the amount of penny:"))

    usr_total_money = (usr_quarter / 4) + (usr_dime / 10) + (usr_nickel / 20) + (usr_penny / 100)
    price = int(menu["latte"]["cost"])
    total_change = usr_total_money - price
    if usr_total_money < price:
        print(f"sorry! you are ${price - usr_total_money} short."
              f"here is your refund of ${usr_total_money}."
              f"try again with more coins.")
    else:
        print(f"you're latte cost ${price} and here is the remaining change ${total_change}")
        print("enjoy you're latte")

def cappuccino():
    """ask usr for coins and check if coins > price and then give latte """

    price = int(menu["cappuccino"]["cost"])
    print(f"price of cappuccino is {price}")
    print("please enter coins!")
    usr_quarter = int(input("enter the amount of quarter:"))
    usr_dime = int(input("enter the amount of dime:"))
    usr_nickel = int(input("enter the amount of nickel:"))
    usr_penny = int(input("enter the amount of penny:"))

    usr_total_money = (usr_quarter / 4) + (usr_dime / 10) + (usr_nickel / 20) + (usr_penny / 100)
    price = int(menu["cappuccino"]["cost"])
    total_change = usr_total_money - price
    if usr_total_money < price:
        print(f"sorry! you are ${price - usr_total_money} short."
              f"here is your refund of ${usr_total_money}."
              f"try again with more coins.")
    else:
        print(f"you're cappuccino cost ${price} and here is the remaining change ${total_change}")
        print("enjoy you're cappuccino")

def resources(water1, milk1, coffee1):
    """this fun. reduces the resources from total resources according to the needs of the drink"""
    global total_resources
    total_resources["water"] = int(total_resources["water"]) - int(water1)
    total_resources["milk"] = int(total_resources["milk"]) - int(milk1)
    total_resources["coffee"] = int(total_resources["coffee"]) - int(coffee1)

def is_sufficient_resource(order_ingredients):
    for item in order_ingredients:
        if total_resources[item] < order_ingredients[item]:
            print(f"sorry there is not enough {item}")
            return True

###################### fn end ###################

print("type 'report' to know the resources\n"
      "type 'off' to stop.\n")

while end:
    print(f"total money collected:${money}")
    usr_flavor = input("what would you like {espresso/latte/cappuccino} ? : ").lower()

    if usr_flavor == "espresso":
        if is_sufficient_resource(menu[usr_flavor]["ingredients"]):
            end = False
        else:
            espresso()
            water = int(menu["espresso"]["ingredients"]["water"])
            milk = int(menu["espresso"]["ingredients"]["milk"])
            coffee = int(menu["espresso"]["ingredients"]["coffee"])
            resources(water, milk, water)
            price1 = int(menu["latte"]["cost"])
            money += price1

    elif usr_flavor == "latte":
        if is_sufficient_resource(menu[usr_flavor]["ingredients"]):
            end = False
        else:
            latte()
            water = int(menu["latte"]["ingredients"]["water"])
            milk = int(menu["latte"]["ingredients"]["milk"])
            coffee = int(menu["latte"]["ingredients"]["coffee"])
            resources(water, milk, water)
            price1 = int(menu["latte"]["cost"])
            money += price1

    elif usr_flavor == "cappuccino":
        if is_sufficient_resource(menu[usr_flavor]["ingredients"]):
            end = False
        else:
            cappuccino()
            water = int(menu["cappuccino"]["ingredients"]["water"])
            milk = int(menu["cappuccino"]["ingredients"]["milk"])
            coffee = int(menu["cappuccino"]["ingredients"]["coffee"])
            resources(water, milk, water)
            price1 = int(menu["latte"]["cost"])
            money += price1

    elif usr_flavor == "off":
        end = False

    elif usr_flavor == "report":
        print(total_resources)