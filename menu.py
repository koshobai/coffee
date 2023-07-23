#
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

buckets = {
    "water":2000,
    "milk":2000,
    "coffee":1000
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
                        if ... #we need something here for checking resources

                    case "espresso":
                        if ... #qualify this first by checking resources

                    case "cappuccino":
                        if ... #qualify this like the above ones

                    case _:
                        print("We don't have enough for that. I can make you something else.")
            print(f"one {order}, right?")
            checkResources(order)
            #print the cost of the item requested
            #define processCoins() for reading, accepting, deducting, and reimbursing coins (i.e. processing)
            #execute the processCoins() function
            def makeDrink(order):
                match order:
                    case "latte":
                        if ... #we need something here for checking resources
                            buckets["water"] -= MENU["latte"]["ingredients"]["water"]
                            buckets["milk"] -= MENU["latte"]["ingredients"]["milk"]
                            buckets["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    case "espresso":
                        if ... #qualify this first by checking resources
                            buckets["water"] -= MENU["espresso"]["ingredients"]["water"]
                            buckets["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    case "cappuccino":
                        if ... #qualify this like the above ones
                            buckets["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                            buckets["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                            buckets["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    case _:
                        print("Something went wrong. Let's try making something else.")
            #execute the makeDrink() function


            break
        elif order == "report":
            print(buckets)
        elif order == "off":
            quit()
        

    except ValueError:
        print("We don't have those. I can make you a latte, an espresso, or a cappuccino.")























# [observation] the each resource is quite limited in supply by default
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#1
order = ""
def prompt(): 
    order = input("what can I get for you?")
    return order
prompt() #I'd like to know how to use the "global" keyword on "order"

#2

"""
Use a while True: loop here that uses try: except ValueError: and else: break
The reason why try: works so well with while True: loops is because
if a user types in trash, we can tell them what we're looking for and 
serve up an input() function to attempt to elicit the correct user response.
"""
if order == "report":
    print(resources)
elif order == "off":
    isOn = False
    exit()
elif order == "latte" or "cappuccino" or "espresso":   
    
    match order:
        case "latte":
            print(f"a {order}...")
            waterLevel = resources.get("water")
            milkLevel = resources.get("milk")
            coffeeLevel = resources.get("coffee")
            
            #we need to check resources: w 200 m 150 c 24 AND 2.5 in user's account
            
            """IF water is insufficient: say we're out of water
               IF milk is insufficient: say we're out of milk
               IF coffee is insufficient: say we're out of coffee beans
               else:"""
            price = str(MENU.get("latte").get("cost"))
            #ask for payment from user
            print(f"That'll be {price}, please...")
                #IF the user has insufficient funds: ask them to come back when they have enough
                #ELSE:
                    #deduct 2.5 from the user and deduct the above from each

        case "cappuccino":
            print(f"a {order}...")
            waterLevel = resources.get("water")

            #we need to check resources: w 250 m 100 c 24 AND 3.0 in user's account
            """IF water is insufficient: say we're out of water
               IF milk is insufficient: say we're out of milk
               IF coffee is insufficient: say we're out of coffee beans
               else:"""
            price = str(MENU.get("cappuccino").get("cost"))
            #ask for payment from user
            print(f"That'll be {price}, please...")
                #IF the user has insufficient funds: ask them to come back when they have enough
                #ELSE:
                    #deduct 3.0 from the user and deduct the above from each

        case "espresso":
            print(f"an {order}...")
            #we need to check resources: w 50 m 0 c 18 AND 1.5 in user's account
            """IF water is insufficient: say we're out of water
               IF milk is insufficient: say we're out of milk
               IF coffee is insufficient: say we're out of coffee beans
               else:"""
            price = str(MENU.get("espresso").get("cost"))
            #ask for payment from user
            print(f"That'll be {price}, please...")
                #IF the user has insufficient funds: ask them to come back when they have enough
                #ELSE:            
                    #deduct 1.5 from the user and deduct the above from each

        case _:
            print("I got nothing for you babe.")
            prompt()

    while resources.water >= 50:
        print("One " + order + ", right? Just a sec...")

else:
    print("You must have messed something up, so try again")
    
#confirm with the resources dictionary 
#that there is enough of each resource to make the user's order

#if any resources are insufficient, output "unavailable"

#if the user does not have enough money, output "you're broke, go home"

#if both conditions are met: accept the money, deplete the supply, 
#add the money to a profit variable, and print "here you go!"

#provide change for any excess amount provided to pay for the drink

#the switch is on by default, and is turned off with the "off" input
isOn = True

reportCurrentStock = print(resources)

# output the report when the user inputs "report"

"""this is a comment
that can be written on two lines"""

"""does this work"""
"""this works
as a big fat comment"""


