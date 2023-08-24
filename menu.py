# menu with espresso, latte, and cappuccino as options
# each option has associated ingredients and an associated cost
# note: anything with a full name is either a global variable
# or a local variable that's explicitly defined inside of a function
# (One can define a variable implicitly when passing it in as an argument too)
def main():

    # the initial number of each denomination is as follows:
    p = 80
    n = 15
    d = 15
    q = 15

    coinpurse = (p*.01)+(n*.05)+(d*.1)+(q*.25)

    # stock initialized arbitrarily

    stock = {
        "water": 2000,
        "milk": 2000,
        "coffee": 1000
    }

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

# I can't call stock anything other than what I've defined above because I'm passing it through
# this program know what cp refers to because I define cp as I'm passing it in as an argument
# I then get to use any word during the function call I want because I didn't define a depended-on global variable

    def report(stock, cp):
        print(f"{stock['water']}, {stock['milk']}, {stock['coffee']}")
        print(f"{cp}")

    def checkResources(ordr):
        match ordr:
            case "latte":
                if stock["water"] >= 200 and stock["milk"] >= 150 and stock["coffee"] >= 24:
                    print("We've got enough here for a latte!")
            case "espresso":
                if stock["water"] >= 50 and stock["coffee"] >= 18:
                    print("We've got enough here for an espresso!")
            case "cappuccino":
                if stock["water"] >= 250 and stock["milk"] >= 100 and stock["coffee"] >= 24:
                    print("We've got enough here for a cappuccino!")
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

    def transact(ordrr, q, d, n, p):
        match ordrr:
            case "latte":
                lattePrice = MENU.get("latte").get("cost")
                print(f"That'll be {lattePrice}, please...")
                while q > 0 and lattePrice > 0:
                    lattePrice -= .25
                    q -= 1
                    if q == 0 or lattePrice == 0:
                        break

                while d > 0 and lattePrice > 0:
                    lattePrice -= .1
                    d -= 1
                    if d == 0 or lattePrice == 0:
                        break
                while n > 0 and lattePrice > 0:
                    lattePrice -= .05
                    n -= 1
                    if n == 0 or lattePrice == 0:
                        break
                while p > 0 and lattePrice > 0:
                    lattePrice -= .01
                    p -= 1
                    if p == 0 or lattePrice == 0:
                        break

            case "cappuccino":
                ccinoPrice = MENU.get("cappuccino").get("cost")
                print(f"That'll be {ccinoPrice}, please...")
                while q > 0 and ccinoPrice > 0:
                    ccinoPrice -= .25
                    q -= 1
                    if q == 0:
                        break
                while d > 0 and ccinoPrice > 0:
                    ccinoPrice -= .1
                    d -= 1
                    if d == 0:
                        break
                while n > 0 and ccinoPrice > 0:
                    ccinoPrice -= .05
                    n -= 1
                    if n == 0:
                        break
                while p > 0 and ccinoPrice > 0:
                    ccinoPrice -= .01
                    p -= 1
                    if p == 0:
                        break
            case "espresso":
                ressoPrice = MENU.get("espresso").get("cost")
                print(f"That'll be {ressoPrice}, please...")
                while q > 0 and ressoPrice > 0:
                    ressoPrice -= .25
                    q -= 1
                    if q == 0:
                        break
                while d > 0 and ressoPrice > 0:
                    ressoPrice -= .1
                    d -= 1
                    if d == 0:
                        break
                while n > 0 and ressoPrice > 0:
                    ressoPrice -= .05
                    n -= 1
                    if n == 0:
                        break
                while p > 0 and ressoPrice > 0:
                    ressoPrice -= .01
                    p -= 1
                    if p == 0:
                        break
            case _:
                print(
                    "Sorry, could you repeat that?")
        return q, d, n, p
        # write the logic for reimbursing coins

    def decrementSupply(oodr):
        match oodr:
            case "latte":
                stock["water"] -= MENU["latte"]["ingredients"]["water"]
                stock["milk"] -= MENU["latte"]["ingredients"]["milk"]
                stock["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            case "espresso":
                stock["water"] -= MENU["espresso"]["ingredients"]["water"]
                stock["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            case "cappuccino":
                stock["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                stock["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                stock["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            case _:
                print(
                    "Something went wrong. Let's try making something else.")
        return stock
    while True:
        try:
            order = input("What'll ya have? ")
            if order == "latte" or order == "cappuccino" or order == "espresso":
                print(f"One {order}, right?")
                checkResources(order)
                checkWallet(q, d, n, p)
                q, d, n, p = transact(order, q, d, n, p)
                # currently the coinpurse is showing 6.8, as if nothing changed
                coinpurse = (p*.01)+(n*.05)+(d*.1)+(q*.25)
                print(f"You have {coinpurse} left in your wallet")
                decrementSupply(order)
                break
            elif order == "report":
                report(stock, coinpurse)
            elif order == "off":
                quit()
            else:
                print("Latte, espresso, or cappuccino please...")
        except ValueError:
            print(
                "We don't have those. I can make you a latte, an espresso, or a cappuccino.")


if __name__ == "__main__":
    main()
