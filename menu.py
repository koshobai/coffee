# menu with espresso, latte, and cappuccino as options
# each option has associated ingredients and an associated cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
# the each resource is quite limited in supply by default
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = input("What would you like?: ").lower()
print("One " + order + ", right? Just a sec...")

#confirm with the resources dictionary 
#that there are enough of each resource to make the user's order

#if any resources are insufficient, output "unavailable"

#if the user does not have enough money, output "you're broke"

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