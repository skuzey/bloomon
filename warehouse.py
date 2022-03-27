class Warehouse:
    # stores quantity for each flower type
    # has convenience methods to add, remove, check quantity

    def __init__(self):
        self.flower_buckets = {}

    # flower_type->count
    def add(self, flower):
        self.flower_buckets[flower] = self.flower_buckets.get(flower, 0) + 1

    def remove(self, flower_type, quantity):
        self.flower_buckets[flower_type] = self.get_quantity(flower_type) - quantity

    def get_quantity(self, flower_type):
        return self.flower_buckets.get(flower_type, 0)

    def fetch(self, combination):
        for flower_type in combination.types():
            self.remove(flower_type, combination.get_quantity(flower_type))

    def contains_all(self, combination):
        for flower_type in combination.types():
            if not (self.contains(flower_type, combination.get_quantity(flower_type))):
                return False
        return True

    def contains(self, flower_type, quantity):
        return self.get_quantity(flower_type) >= quantity
