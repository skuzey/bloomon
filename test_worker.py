import unittest

from design import Design
from worker import Worker


class WorkerTests(unittest.TestCase):

    def test_simple(self):
        designs = [Design("AS2a2b3"), Design("BL2a2")]
        worker = Worker(designs)

        self.assertEqual("", worker.flower_received("aL"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("aS"))
        self.assertEqual("AS1a2b", worker.flower_received("bS"))

        self.assertEqual("", worker.flower_received("aS"))
        self.assertEqual("BL2a", worker.flower_received("aL"))
        self.assertEqual("", worker.flower_received("aS"))
        self.assertEqual("AS2a1b", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("aL"))
        self.assertEqual("BL2a", worker.flower_received("aL"))

    def test_max_quantities_are_honoured(self):
        designs = [Design("AS2a1b3"), Design("BL2a2")]
        worker = Worker(designs)

        self.assertEqual("", worker.flower_received("aL"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("aS"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("AS2a1b", worker.flower_received("aS"))

    def test_complex(self):
        designs = [Design("AS2a2"), Design("BS2a1b3c2d6")]
        worker = Worker(designs)

        self.assertEqual("", worker.flower_received("aS"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("AS2a", worker.flower_received("aS"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("bS"))
        self.assertEqual("", worker.flower_received("cS"))
        self.assertEqual("", worker.flower_received("cS"))
        self.assertEqual("", worker.flower_received("dS"))
        self.assertEqual("", worker.flower_received("cS"))
        self.assertEqual("BS1a1b3c1d", worker.flower_received("aS"))


if __name__ == '__main__':
    unittest.main()
