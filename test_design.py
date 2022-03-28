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

    def test_generate_combinations(self):
        flower_types = {"a": 6, "b": 4, "c": 2, "d": 1}

        result = DesignCombinationGenerator().generate(flower_types, 4)

        # expected = ["aaaa","aaab","aaac","aabb","aabc","abbb","abbc","bbbc"]
        print("list: ", result)

        self.assertEqual(8, len(result))

        self.assertEqual(5, result[0].get_quantity("a"))
        self.assertEqual(1, result[0].get_quantity("b"))
        self.assertEqual(1, result[0].get_quantity("c"))
        self.assertEqual(1, result[0].get_quantity("d"))

        self.assertEqual(4, result[1].get_quantity("a"))
        self.assertEqual(2, result[1].get_quantity("b"))
        self.assertEqual(1, result[1].get_quantity("c"))
        self.assertEqual(1, result[1].get_quantity("d"))

        self.assertEqual(4, result[2].get_quantity("a"))
        self.assertEqual(1, result[2].get_quantity("b"))
        self.assertEqual(2, result[2].get_quantity("c"))
        self.assertEqual(1, result[2].get_quantity("d"))

        self.assertEqual(3, result[3].get_quantity("a"))
        self.assertEqual(3, result[3].get_quantity("b"))
        self.assertEqual(1, result[3].get_quantity("c"))
        self.assertEqual(1, result[3].get_quantity("d"))

        self.assertEqual(1, result[7].get_quantity("a"))
        self.assertEqual(4, result[7].get_quantity("b"))
        self.assertEqual(2, result[7].get_quantity("c"))
        self.assertEqual(1, result[7].get_quantity("d"))

    def test_design_with_two_digit_flower_quantities(self):
        design = Design("AS12a3b14")

        self.assertEqual(["12a2b", "11a3b"],
                         [str(x) for x in design.combinations])


if __name__ == '__main__':
    unittest.main()
