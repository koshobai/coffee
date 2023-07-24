# menu with espresso, latte, and cappuccino as options
# each option has associated ingredients and an associated cost
def main():
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

    # the initial number of each denomination is as follows:
    p = 80
    n = 15
    d = 15
    q = 15

    # the worth of each denomination is determined through multiplication
    wallet = {
        denominations["pennies"] * p,
        denominations["nickels"] * n,
        denominations["dimes"] * d,
        denominations["quarters"] * q
    }

    # retrieves the keys of each resource for use in the if statement order confirmation gate
    resourceList = list(buckets.keys())

    w = resourceList["water"]
    m = resourceList["milk"]
    c = resourceList["coffee"]

    while True:
        try:
            order = input("What'll ya have?")
            if order == w or m or c:
                print(f"One {order}, right?")
                checkResources(order)
                transact(order)
                decrementSupply(order)
            elif order == "report":
                print(buckets)
            elif order == "off":
                quit()
            else:
                print("Latte, espresso, or cappuccino please...")
        except ValueError:
            print(
                "We don't have those. I can make you a latte, an espresso, or a cappuccino.")

        while True:
            try:
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

                def transact(order):
                    # write the logic for reading, accepting, deducting, and reimbursing coins (i.e. processing)
                    # print the cost of the item requested
                    # ask for payment from user
                    # if the user does not have enough money, output "you're broke, go home"

                    # ELSE:
                    # deduct 2.5,3.0, or 1.5 from the user and deduct the above from each
                    match order:
                        case "latte":
                            lattePrice = str(MENU.get("latte").get("cost"))
                            print(f"That'll be {lattePrice}, please...")
                            break
                        case "espresso":
                            ccinoPrice = str(
                                MENU.get("cappuccino").get("cost"))
                            print(f"That'll be {ccinoPrice}, please...")
                            break
                        case "cappuccino":
                            ressoPrice = str(MENU.get("espresso").get("cost"))
                            print(f"That'll be {ressoPrice}, please...")
                            break
                        case _:
                            print(
                                "We don't have enough for that. I can make you something else.")

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


if __name__ == "__main__":
    main()
