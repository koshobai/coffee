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


