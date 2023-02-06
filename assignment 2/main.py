import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


open = True
available = False

while open:
    order = input ("What would you like? (small/medium/large/off/report): ")
    if order == "small":
        print("You chose Small")
        avilable = sandwich_maker_instance.check_resources(recipes["small"])
        if avilable:
            payment = cashier_instance.process_coins()
            cost = recipes["small"]["cost"]

            possible = cashier_instance.transaction_result(payment, recipes["small"]["cost"])
            if possible:
                sandwich_maker_instance.make_sandwich("small", recipes["small"]["ingredients"])
                print("Your change is", payment-cost)
                print("Your small sandwich is ready. are you sure you don't want more")
            if possible == False:
                print("sorry that's not enough money")
    if order == "medium":
        print("You chose Medium")
        avilable = sandwich_maker_instance.check_resources(recipes["medium"])
        if avilable:
            payment = cashier_instance.process_coins()
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
        available = sandwich_maker_instance.check_resources(recipes["large"])
        if avilable:
            payment = cashier_instance.process_coins()
            cost = recipes["large"]["cost"]

            possible = cashier_instance.transaction_result(payment, recipes["large"]["cost"])
            if possible:
                sandwich_maker_instance.make_sandwich("large", recipes["large"]["ingredients"])
                print("Your change is", payment-cost)
                print("Your large sandwich is ready")
                print("thats a big sandwich")
            if possible == False:
                print("sorry that's not enough money")
                print("what should we add")
                print("Have a good day")
    if order == "report":
        print("Ok boss")

        if order == "off":
            open = False






