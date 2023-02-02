### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        bread = self.machine_resources['bread'] - ingredients['ingredients']['bread']
        ham = self.machine_resources['ham'] - ingredients['ingredients']['ham']
        cheese = self.machine_resources['cheese'] - ingredients['ingredients']['cheese']

        if bread <=  0:
            print("Not enough bread. ")
            return False
        if ham <= 0:
            print("Not enough ham. ")
            return False
        if cheese <= 0:
            print("Not enough cheese.")
            return False
        return True




    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please Enter your coins")
        coins = 0.00

        dollars = input("How many whole dollars?:")
        d = float(dollars)
        coins = coins + d

        half_dollars = input("How many half dollars?:")
        h = float(half_dollars)
        coins = coins + (h*.5)

        quarters = input("how many Quarters?: ")
        q = float(quarters)
        coins = coins + (q * .25)

        nickles = input("how many nickels?: ")
        n= float(nickles)
        coins = coins + (n*.05)
        return coins


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        if coins < cost:
            return False


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources['bread'] = self.machine_resources['bread']-order_ingredients['bread']
        self.machine_resources['ham'] = self.machine_resources['ham']-order_ingredients['ham']
        self.machine_resources['cheese'] = self.machine_resources['cheese'] - order_ingredients['cheese']

sandwichMachine = SandwichMachine(resources)
open = True
available = False

while open:
    order = input ("What would you like? (small/medium/large/off/report): ")
    if order == "small":
        print("You chose Small")
        available = sandwichMachine.check_resources(recipes["small"])
        if available:
            payment = sandwichMachine.process_coins()
            cost = recipes["small"]["cost"]

            possible = sandwichMachine.transaction_result(payment, recipes["small"]["cost"])
            if possible:
                sandwichMachine.make_sandwich("small", recipes["small"]["ingredients"])
                print("Your change is", payment-cost)
                print("Your small sandwich is ready. are you sure you don't want more")
            if possible == False:
                print("sorry that's not enough money")
    if order == "medium":
        print("You chose Medium")
        available = sandwichMachine.check_resources(recipes["medium"])
        if available:
            payment = sandwichMachine.process_coins()
            cost = recipes["medium"]["cost"]

            possible = sandwichMachine.transaction_result(payment, recipes["medium"]["cost"])
            if possible:
                sandwichMachine.make_sandwich("medium", recipes["medium"]["ingredients"])
                print("Your change is", payment-cost)
                print("Your medium sandwich is ready.")
                print("Right size")
            if possible == False:
                print("sorry that's not enough money")

    if order == "large":
        print("You chose large")
        available = sandwichMachine.check_resources(recipes["large"])
        if available:
            payment = sandwichMachine.process_coins()
            cost = recipes["large"]["cost"]

            possible = sandwichMachine.transaction_result(payment, recipes["large"]["cost"])
            if possible:
                sandwichMachine.make_sandwich("large", recipes["large"]["ingredients"])
                print("Your change is", payment-cost)
                print("Your large sandwich is ready")
            if possible == False:
                print("sorry that's not enough money")
                print("Have a good day")
    if order == "report":

        if order == "off":
            open = False






