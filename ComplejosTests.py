import unittest
import ComplejosLibreria as cl

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        c1 = (2, 5)
        c2 = (-1, 7)
        self.assertEqual(cl.suma(c1, c2), (1, 12))

    def test_prod(self):
        c1 = (5, 2)
        c2 = (1, 9)
        self.assertEqual(cl.producto(c1, c2), (-13, 47))

    def test_resta(self):
        c1 = (7, 2)
        c2 = (2, -5)
        self.assertEqual(cl.resta(c1, c2), (5, 7))

    def test_cjg(self):
        c = (3, 9)
        self.assertEqual(cl.conjugado(c), (3, -9))

    def test_div(self):
        c1 = (3, 5)
        c2 = (4, 9)
        self.assertEqual(cl.division(c1, c2), (57/97, -7/97))

    def test_mod(self):
        c = (3,4)
        self.assertEqual(cl.modulo(c), 5)

    def test_fase(self):
        c = (2, 5)
        self.assertEqual(cl.fase(c), 1.1902899496825317)

    def test_c_a_p(self):
        c = ((2)**(1/2)/2, (2)**(1/2)/2)
        self.assertEqual(cl.cart_a_pol(c), (1, 0.7853981633974483))

    def test_p_a_c(self):
        c = (5, 0.927295218001612)
        self.assertEqual(cl.pol_a_cart(c), (3, 4))

if __name__ == '__main__':
    unittest.main()
