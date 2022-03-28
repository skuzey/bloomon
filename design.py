import re


class DesignCombination:
    # sample: {aS:4, bS:1}, {aS:3, bS:2}

    def __init__(self, flower_types):
        self.map = {}
        for fType in flower_types:
            self.map[fType] = 1

    def get_quantity(self, f_type):
        return self.map.get(f_type)

    def increment(self, f_type):
        self.map[f_type] = self.map.get(f_type, 0) + 1

    def types(self):
        return self.map.keys()

    def to_string(self):
        result = ""
        for f_type in self.types():
            result += str(self.get_quantity(f_type)) + str(f_type[0])
        return result

    def __repr__(self):
        return self.to_string()

    def __hash__(self):
        return hash(self.to_string())

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.to_string() == other.to_string()


class DesignCombinationGenerator:
    # sample: {aS:4, bS:1}, {aS:3, bS:2}
    def __init__(self):
        self.combinations = []

    def generate(self, flower_types, k):
        arr = self.convert_flower_types_to_char_arr(flower_types)
        self.generate_combinations(arr, 0, len(arr) - 1, [None] * k, 0, k, flower_types.keys())
        return self.combinations

    # converts {a:2, b:3, c:1} into [a,b,b]
    def convert_flower_types_to_char_arr(self, flower_types):
        exploded = []
        for f_type in flower_types:
            # generate only optional types
            exploded += [f_type] * (flower_types.get(f_type) - 1)
        return exploded

    def generate_combinations(self, arr, start, end, data, index, combination_size, flower_types):
        # Current combination is ready, save it
        if index == combination_size:
            combination = self.create_combination(data, flower_types)
            if combination not in self.combinations:
                self.combinations.append(combination)
            return

        # Replace index with all possible elements.
        for i in range(start, end + 1):
            data[index] = arr[i]
            self.generate_combinations(arr, i + 1, end, data, index + 1, combination_size, flower_types)

    def create_combination(self, data, flower_types):
        dc = DesignCombination(flower_types)  # we need min 1 flower for each type, constructor handles it

        # each turn, increase the quantity of the flower by one
        for f_type in data:
            dc.increment(f_type)
        return dc


class Design:
    # Data class to parse and hold the values that come with a design string
    # e.g AS2a3b4 turns into id:A, size:S, totalFlowerCount:4, flowerTypes[aS:2, bS:3]

    def __init__(self, design_str):
        self.id = None
        self.size = None
        self.total_flower_count = 0

        # flower types in this design : {aL:2, bL:1}
        self.flower_types = {}

        self.parse(design_str)

        self.combinations = DesignCombinationGenerator().generate(
            self.flower_types,
            self.total_flower_count - len(self.flower_types),
        )

    def parse(self, design_str):
        self.id = design_str[0]
        self.size = design_str[1]
        total_count_str = re.findall(r"(\d+)$", design_str)[0]
        self.total_flower_count = int(total_count_str)
        total_count_size = len(total_count_str)
        flower_types_str = design_str[2:-total_count_size]
        groups = re.findall(r"[\d]+[a-z]*", flower_types_str)  # split by 2 chars
        for group in groups:
            flower_type = group[-1]
            quantity = int(group[0:-1])
            self.flower_types[flower_type + self.size] = quantity
