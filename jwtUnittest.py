import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('soap'.upper(), 'SOAP')
  def test_equal(self):
      self.assertEqual('$ebffc391615e1b1ccc99a5621a10a65303eaee','$ebffc391615e1b1ccc99a5621a10a65303eaee')

  def test_islower(self):
      self.assertTrue('soap'.islower())
      self.assertFalse('Soap'.islower())

 # def test_split(self):
     # s = 'hello world'
     # self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
     # with self.assertRaises(TypeError):
         #` s.split(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
