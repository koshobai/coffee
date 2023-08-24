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

    # retrieves the keys of each resource for use in the if statement order confirmation gate
    resourceList = list(buckets.keys())

    w = resourceList[0]
    m = resourceList[1]
    c = resourceList[2]

    # the initial number of each denomination is as follows:
    p = 80
    n = 15
    d = 15
    q = 15

    coinpurse = (p*.01)+(n*.05)+(d*.1)+(q*.25)

    def report(buckets, cp):
        print(f"{buckets['water']}, {buckets['milk']}, {buckets['coffee']}")
        print(f"{cp}")

    def checkResources(order):
        match order:
            case "latte":
                if buckets["water"] >= 200 and buckets["milk"] >= 150 and buckets["coffee"] >= 24:
                    print("this")
            case "espresso":
                if buckets["water"] >= 50 and buckets["coffee"] >= 18:
                    print("this")
            case "cappuccino":
                if buckets["water"] >= 250 and buckets["milk"] >= 100 and buckets["coffee"] >= 24:
                    print("this")
            case _:
                print(
                    "We don't have enough for that. I can make you something else.")

    def checkWallet(q, d, n, p):
        # user's wallet contains coins in US currency of varying denominations
        denominations = {
            "pennies": 0.01,
            "nickels": 0.05,
            "dimes": 0.1,
            "quarters": 0.25
        }
    # the worth of each denomination is determined through multiplication
        totalCash = (denominations["pennies"] * p) + (denominations["nickels"] * n) + (
            denominations["dimes"] * d) + (denominations["quarters"] * q)
        print(f"Seems like you have {totalCash} on you...")

    def transact(order, q, d, n, p):
        match order:
            case "latte":
                lattePrice = MENU.get("latte").get("cost")
                print(f"That'll be {lattePrice}, please...")
                while q > 0 and lattePrice > 0:
                    lattePrice -= .25
                    q -= q
                while d > 0 and lattePrice > 0:
                    lattePrice -= .1
                    d -= d
                while n > 0 and lattePrice > 0:
                    lattePrice -= .05
                    n -= n
                while p > 0 and lattePrice > 0:
                    lattePrice -= .01
                    p -= p
            case "cappuccino":
                ccinoPrice = MENU.get("cappuccino").get("cost")
                print(f"That'll be {ccinoPrice}, please...")
                while q > 0 and ccinoPrice > 0:
                    ccinoPrice -= .25
                    q -= q
                while d > 0 and ccinoPrice > 0:
                    ccinoPrice -= .1
                    d -= d
                while n > 0 and ccinoPrice > 0:
                    ccinoPrice -= .05
                    n -= n
                while p > 0 and ccinoPrice > 0:
                    ccinoPrice -= .01
                    p -= p
            case "espresso":
                ressoPrice = MENU.get("espresso").get("cost")
                print(f"That'll be {ressoPrice}, please...")
                while q > 0 and ressoPrice > 0:
                    ressoPrice -= .25
                    q -= q
                while d > 0 and ressoPrice > 0:
                    ressoPrice -= .1
                    d -= d
                while n > 0 and ressoPrice > 0:
                    ressoPrice -= .05
                    n -= n
                while p > 0 and ressoPrice > 0:
                    ressoPrice -= .01
                    p -= p
            case _:
                print(
                    "Sorry, could you repeat that?")

        # write the logic for reimbursing coins

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

    while True:
        try:
            order = input("What'll ya have? ")
            if order == "latte" or order == "cappuccino" or order == "espresso":
                print(f"One {order}, right?")
                checkResources(order)
                checkWallet(q, d, n, p)
                transact(order, q, d, n, p)
                decrementSupply(order)
                break
            elif order == "report":
                report(buckets, coinpurse)
            elif order == "off":
                quit()
            else:
                print("Latte, espresso, or cappuccino please...")
        except ValueError:
            print(
                "We don't have those. I can make you a latte, an espresso, or a cappuccino.")


if __name__ == "__main__":
    main()
