from warehouse import Warehouse


class Worker:
    # This class processes every incoming flower (like a real worker in the warehouse) and
    # creates a Bouquet if possible, removing used flowers from the warehouse

    def __init__(self, designs):
        self.wh = Warehouse()
        self.designs = designs

    def flower_received(self, flower):

        self.wh.add(flower)
        return self.process()

    def process(self):

        for design in self.designs:
            for combination in design.combinations:
                if self.wh.contains_all(combination):
                    return self.create_bouquet(combination, design)

        return ""

    def create_bouquet(self, combination, design):

        self.wh.fetch(combination)
        return design.id + design.size + str(combination)
