import unittest
import kerberosauthentication

class TestMyScript(unittest.TestCase):

        def test_has_kerberos_ticket(self):# true or false if they have the kerberos ticket
                self.assertTrue('FOO'.has_kerberos_ticket())
                self.assertFalse('Foo'.has_kerberos_ticket())


        def test_issueJwt(self):#ISSUE THE JWT
                self.assertTrue('FOO'.issueJwt())
                self.assertFalse('foo'.issueJwt())

        def test_decodeJwt(self):#DECODED JWT
                self.assertEqual('foo'.decodeJwt(), 'Foo')

        def test_kinit(self):#TRUE OR FALSE USER
                self.assertTrue('FOO'.kinit())
                self.assertFalse('Foo'.kinit())

        def test_StartProcess(self):#PROCESS AUTH OR NOT
                self.assertTrue('FOO'.StartProcess())
                self.assertFalse('Foo'.StartProcess())

        if __name__ == '__main__':
                unittest.main()
