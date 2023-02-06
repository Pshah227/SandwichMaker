class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        bread = self.machine_resources['bread'] - ingredients['ingredients']['bread']
        ham = self.machine_resources['ham'] - ingredients['ingredients']['ham']
        cheese = self.machine_resources['cheese'] - ingredients['ingredients']['cheese']

        if bread <= 0:
            print("Not enough bread. ")
            return False
        if ham <= 0:
            print("Not enough ham. ")
            return False
        if cheese <= 0:
            print("Not enough cheese.")
            return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
                  Hint: no output"""
        self.machine_resources['bread'] = self.machine_resources['bread'] - order_ingredients['bread']
        self.machine_resources['ham'] = self.machine_resources['ham'] - order_ingredients['ham']
        self.machine_resources['cheese'] = self.machine_resources['cheese'] - order_ingredients['cheese']
