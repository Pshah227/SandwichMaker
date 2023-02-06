class Cashier:
    def __init__(self):
        pass

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
                  Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        if coins < cost:
            return False

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
    n = float(nickles)
    coins = coins + (n*.05)
    print("you got $ ", coins)



