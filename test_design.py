import unittest

from design import DesignCombinationGenerator, Design


class DesignTests(unittest.TestCase):

    def test_design(self):
        design = Design("AS6a4b2c7")

        self.assertEqual(["5a1b1c", "4a2b1c", "4a1b2c", "3a3b1c", "3a2b2c", "2a4b1c", "2a3b2c", "1a4b2c"],
                         [str(x) for x in design.combinations])

        design = Design("AS2a3b1c2d6")
        self.assertEqual(["2a2b1c1d", "2a1b1c2d", "1a3b1c1d", "1a2b1c2d"],
                         [str(x) for x in design.combinations])

        design = Design("AS2a2b3")
        self.assertEqual(["2a1b", "1a2b"], [str(x) for x in design.combinations])

    def test_design_with_two_digit_flower_quantities(self):
        design = Design("AS12a3b14")

        self.assertEqual(["12a2b", "11a3b"],
                         [str(x) for x in design.combinations])

    def test_generate_combinations(self):
        flower_types = {"a": 6, "b": 4, "c": 2, "d": 1}

        result = DesignCombinationGenerator().generate(flower_types, 4)

        print("list: ", result)

        self.assertEqual(8, len(result))

        self.assertEqual({'a': 5, 'b': 1, 'c': 1, 'd': 1}, result[0].get_quantities())
        self.assertEqual({'a': 4, 'b': 2, 'c': 1, 'd': 1}, result[1].get_quantities())
        self.assertEqual({'a': 4, 'b': 1, 'c': 2, 'd': 1}, result[2].get_quantities())
        self.assertEqual({'a': 3, 'b': 3, 'c': 1, 'd': 1}, result[3].get_quantities())
        self.assertEqual({'a': 1, 'b': 4, 'c': 2, 'd': 1}, result[7].get_quantities())


if __name__ == '__main__':
    unittest.main()
