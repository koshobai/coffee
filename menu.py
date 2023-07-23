# menu with espresso, latte, and cappuccino as options
# each option has associated ingredients and an associated cost
MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
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
# stock initialized arbitrarily
buckets = {
    "water": 2000,
    "milk": 2000,
    "coffee": 1000
}

# user's wallet contains coins in US currency of varying denominations
denominations = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.1,
    "quarters": 0.25
}

p = 80
n = 15
d = 15
q = 15

wallet = {
    denominations["pennies"] * p,
    denominations["nickels"] * n,
    denominations["dimes"] * d,
    denominations["quarters"] * q
}

resourceList = list(buckets.keys())

w = resourceList["water"]
m = resourceList["milk"]
c = resourceList["coffee"]

while True:
    try:
        order = input("What'll ya have?")
        if order == w or m or c:
            def checkResources(order):
                match order:
                    case "latte":
                        if buckets["water"] >= 200 and buckets["milk"] >= 150 and buckets["water"] >= 24:
                            print("this")
                            break
                    case "espresso":
                        if buckets["water"] >= 50 and buckets["water"] >= 18:
                            print("this")
                            break
                    case "cappuccino":
                        if buckets["water"] >= 250 and buckets["milk"] >= 100 and buckets["water"] >= 24:
                            print("this")
                            break
                    case _:
                        print(
                            "We don't have enough for that. I can make you something else.")
            print(f"One {order}, right?")
            checkResources(order)
        elif order == "report":
            print(buckets)
        elif order == "off":
            quit()
        else:
            print("Latte, espresso, or cappuccino please...")
    except ValueError:
        print("We don't have those. I can make you a latte, an espresso, or a cappuccino.")

    # print the cost of the item requested
    # define processCoins() for reading, accepting, deducting, and reimbursing coins (i.e. processing)
    # execute the processCoins() function... OR just use if statements
    while True:
        try:

            def decrementSupply(order):
                match order:
                    case "latte":
                        buckets["water"] -= MENU["latte"]["ingredients"]["water"]
                        buckets["milk"] -= MENU["latte"]["ingredients"]["milk"]
                        buckets["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    case "espresso":
                        buckets["water"] -= MENU["espresso"]["ingredients"]["water"]
                        buckets["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    case "cappuccino":
                        buckets["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                        buckets["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                        buckets["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    case _:
                        print(
                            "Something went wrong. Let's try making something else.")
        except ValueError:
            print(
                "We don't have those. I can make you a latte, an espresso, or a cappuccino.")

            # execute the decrementSupply() function
            decrementSupply(order)

            price = str(MENU.get("latte").get("cost"))
            # ask for payment from user
            print(f"That'll be {price}, please...")
            # IF the user has insufficient funds: ask them to come back when they have enough
            # ELSE:
            # deduct 2.5 from the user and deduct the above from each

            # we need to check resources: w 250 m 100 c 24 AND 3.0 in user's account
            """IF water is insufficient: say we're out of water
               IF milk is insufficient: say we're out of milk
               IF coffee is insufficient: say we're out of coffee beans
               else:"""
            price = str(MENU.get("cappuccino").get("cost"))
            # ask for payment from user
            print(f"That'll be {price}, please...")
            # IF the user has insufficient funds: ask them to come back when they have enough
            # ELSE:
            # deduct 3.0 from the user and deduct the above from each

            price = str(MENU.get("espresso").get("cost"))
            # ask for payment from user
            print(f"That'll be {price}, please...")
            # IF the user has insufficient funds: ask them to come back when they have enough
            # ELSE:
            # deduct 1.5 from the user and deduct the above from each


# confirm with the resources dictionary
# that there is enough of each resource to make the user's order

# if any resources are insufficient, output "unavailable"

# if the user does not have enough money, output "you're broke, go home"

# if both conditions are met: accept the money, deplete the supply,
# add the money to a profit variable, and print "here you go!"

# provide change for any excess amount provided to pay for the drink

# the switch is on by default, and is turned off with the "off" input
